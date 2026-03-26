# RFC-001: Infraestructura Segura — Web en Oracle Cloud VPS

**Estado:** Propuesta (revisada)
**Versión:** 1.1
**Fecha:** 2026-03-26
**Autor:** M1L0_J05
**Revisión:** Corregido para stack real (Docker + Caddy), estado actual del VPS, y buenas prácticas

---

## 1. Resumen Ejecutivo

Este documento define el plan de implementación para desplegar una aplicación web en un VPS de Oracle Cloud Free Tier con superficie de ataque mínima. La arquitectura se basa en **4 capas de seguridad en serie**: Cloudflare WAF como frontal público, Oracle Security List como firewall de red, iptables como firewall de host, y Fail2ban como detección de abuso. El acceso administrativo se canaliza exclusivamente a través de Tailscale, sin exponer SSH al exterior en ningún momento.

La aplicación se despliega con **Docker Compose** (Caddy como reverse proxy + app Reflex), por lo que las reglas de firewall a nivel de host deben contemplar las cadenas de iptables que Docker gestiona (DOCKER-USER).

---

## 2. Arquitectura Objetivo

```
[Internet / Usuario]
        │
        ▼
┌───────────────────────────────┐
│  CAPA 1 — Cloudflare          │  WAF, DDoS, proxy inverso,
│  Free Tier (Proxy + WAF)      │  IP de Oracle oculta
└──────────────┬────────────────┘
               │ Solo rangos IP de Cloudflare
               ▼
┌───────────────────────────────┐
│  CAPA 2 — Oracle Security     │  TCP 80 y TCP 443 únicamente
│  List (VCN Firewall)          │  Todo lo demás: denegado
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│  CAPA 3 — iptables + ipset    │  Whitelist rangos Cloudflare
│  (Host Firewall)              │  DOCKER-USER + INPUT
│                               │  DROP si origen no es CF
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│  CAPA 4 — Fail2ban            │  Baneos progresivos por logs
│  (Detección de abuso)         │  Jails SSH + Caddy
└──────────────┬────────────────┘
               │
               ▼
┌───────────────────────────────┐
│  Docker Compose               │
│  ┌─────────┐  ┌─────────────┐│
│  │  Caddy   │→│  App Reflex ││
│  │ :80/:443 │  │    :8000    ││
│  └─────────┘  └─────────────┘│
└───────────────────────────────┘

[Administrador] ──► Tailscale DERP ──► SSH (solo interfaz tailscale0)
```

---

## 3. Prerrequisitos

| Componente | Requisito | Estado |
| :-- | :-- | :-- |
| VPS Oracle Cloud Free Tier | Provisionado y accesible por SSH | ✅ Completado |
| SO del VPS | Ubuntu 22.04 / 24.04 LTS actualizado | ✅ Completado |
| Docker + Docker Compose | Instalado en el VPS | ✅ Completado |
| Tailscale | Instalado y conectado en local + VPS | ✅ Completado |
| SSH con llaves RSA | Autenticación por clave pública configurada | ✅ Completado |
| Dominio propio | Nameservers apuntando a Cloudflare | Pendiente |
| Cuenta Cloudflare (free) | Dominio añadido y verificado | Pendiente |

---

## 4. Fases de Implementación

### FASE 1 — Acceso Administrativo Seguro (Tailscale) ✅ COMPLETADA

**Objetivo:** Establecer el canal de administración antes de cerrar cualquier cosa. Esta fase es bloqueante — no se puede proceder a la Fase 2 sin completarla y verificarla.

**Estado actual:** Tailscale instalado y conectado en ambos extremos (local + VPS). SSH funciona con autenticación por llaves RSA vía Tailscale.

**Paso pendiente:** Restringir SSH a la interfaz Tailscale únicamente:
```bash
# Con la sesión Tailscale ya abierta y verificada:
sudo nano /etc/ssh/sshd_config
# Añadir/modificar:
#   ListenAddress 100.x.y.z    ← IP Tailscale del VPS
sudo systemctl restart sshd
```

> **⚠️ IMPORTANTE:** Verificar desde una **segunda terminal** que SSH via Tailscale funciona antes de cerrar la sesión original.

**Criterio de éxito:** `ssh usuario@IP_PUBLICA_ORACLE` = timeout. `ssh usuario@100.x.y.z` = login OK.

---

### FASE 2 — Firewall de Red (Oracle Security List)

**Objetivo:** Cerrar todos los puertos en la VCN de Oracle dejando solo tráfico web público.

**En la consola Oracle:** `Networking → VCN → Security Lists → Default Security List`

**Reglas de Ingress a mantener/crear:**

| Puerto | Protocolo | Origen | Propósito |
| :-- | :-- | :-- | :-- |
| 80 | TCP | 0.0.0.0/0 | HTTP (CF redirige a HTTPS) |
| 443 | TCP | 0.0.0.0/0 | HTTPS Cloudflare → Caddy |

**Reglas a eliminar:**

- Cualquier regla con puerto 22 abierto a `0.0.0.0/0`
- Reglas `All Traffic` si existen
- UDP 41641 — **no necesario**, Tailscale usa relay DERP vía 443 saliente

**Criterio de éxito:** `nmap -p 22 IP_ORACLE` desde internet = `filtered`.

---

### FASE 3 — Firewall de Host (iptables + ipset)

**Objetivo:** Segunda línea de defensa a nivel SO. Solo las IPs de Cloudflare pueden alcanzar los puertos 80/443.

> **⚠️ IMPORTANTE — Docker y iptables:** Docker gestiona sus propias cadenas de iptables. El tráfico destinado a contenedores **NO pasa por la cadena INPUT**, sino por **DOCKER-USER → FORWARD**. Por tanto, las reglas de whitelist de Cloudflare deben aplicarse tanto en INPUT como en DOCKER-USER.
>
> **NO ejecutar `iptables -F INPUT`** — Oracle Cloud Ubuntu tiene reglas preconfiguradas para la VCN. Hacer flush puede causar pérdida de conectividad.

```bash
# Instalar dependencias
sudo apt install -y ipset iptables-persistent

# Crear ipset con rangos oficiales de Cloudflare
sudo ipset create cloudflare hash:net
for ip in \
  173.245.48.0/20 103.21.244.0/22 103.22.200.0/22 103.31.4.0/22 \
  141.101.64.0/18 108.162.192.0/18 190.93.240.0/20 188.114.96.0/20 \
  197.234.240.0/22 198.41.128.0/17 162.158.0.0/15 104.16.0.0/13 \
  104.24.0.0/14 172.64.0.0/13 131.0.72.0/22; do
  sudo ipset add cloudflare $ip
done

# ── Reglas INPUT (tráfico directo al host) ──
# Permitir loopback y conexiones establecidas
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
# Permitir todo el tráfico vía Tailscale (administración)
sudo iptables -A INPUT -i tailscale0 -j ACCEPT
# Permitir HTTP/HTTPS solo desde IPs de Cloudflare
sudo iptables -A INPUT -p tcp --dport 80  -m set --match-set cloudflare src -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -m set --match-set cloudflare src -j ACCEPT
# Denegar todo lo demás (añadir al final, sin flush)
sudo iptables -A INPUT -j DROP

# ── Reglas DOCKER-USER (tráfico a contenedores) ──
# Docker crea esta cadena automáticamente. Las reglas aquí filtran
# ANTES de que Docker haga NAT al contenedor.
sudo iptables -I DOCKER-USER -m set --match-set cloudflare src -j RETURN
sudo iptables -I DOCKER-USER -i tailscale0 -j RETURN
sudo iptables -I DOCKER-USER -m conntrack --ctstate ESTABLISHED,RELATED -j RETURN
# DROP todo lo demás dirigido a contenedores (insertar ANTES del RETURN final)
sudo iptables -A DOCKER-USER -j DROP

# Persistir reglas e ipset
sudo ipset save | sudo tee /etc/ipset.conf
sudo netfilter-persistent save
```

**Restauración automática del ipset tras reinicio** — crear servicio systemd (rc.local no existe en Ubuntu moderno):

```bash
sudo tee /etc/systemd/system/ipset-restore.service << 'EOF'
[Unit]
Description=Restaurar ipset desde configuración guardada
Before=netfilter-persistent.service docker.service

[Service]
Type=oneshot
ExecStart=/sbin/ipset restore -f /etc/ipset.conf
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable ipset-restore.service
```

**Script de actualización semanal de IPs Cloudflare:**

```bash
sudo tee /usr/local/bin/update-cf-ips.sh << 'SCRIPT'
#!/bin/bash
# Actualizar rangos IP de Cloudflare en ipset
set -euo pipefail
ipset flush cloudflare
while read -r ip; do
  ipset add cloudflare "$ip"
done < <(curl -s https://www.cloudflare.com/ips-v4)
ipset save > /etc/ipset.conf
logger "ipset cloudflare actualizado correctamente"
SCRIPT

sudo chmod +x /usr/local/bin/update-cf-ips.sh
```

```bash
# Programar ejecución semanal (lunes 3:00 AM)
echo "0 3 * * 1 root /usr/local/bin/update-cf-ips.sh" \
  | sudo tee /etc/cron.d/update-cf-ips
```

**Criterio de éxito:** `curl http://IP_ORACLE` desde internet (IP no-CF) = timeout.

---

### FASE 4 — Fail2ban

**Objetivo:** Detección y baneo automático de abuso con escalado temporal progresivo.

> **Nota sobre Caddy en Docker:** Para que Fail2ban (en el host) pueda leer los logs de Caddy (en el contenedor), es necesario que Caddy escriba sus access logs en un volumen montado accesible desde el host. El `compose.yaml` debe incluir un volumen para logs.

**4.1 — Configurar logs de Caddy:**

Añadir al `Caddyfile` la directiva de logging:
```
{
    log {
        output file /var/log/caddy/access.log {
            roll_size 50MiB
            roll_keep 5
        }
        format json
    }
}
```

Añadir volumen en `compose.yaml` para el servicio `caddy`:
```yaml
volumes:
  - caddy_logs:/var/log/caddy

# Y montar en el host para que Fail2ban pueda leerlo:
# En la sección volumes del nivel superior:
volumes:
  caddy_logs:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: /var/log/caddy
```

Crear el directorio en el host:
```bash
sudo mkdir -p /var/log/caddy
```

**4.2 — Instalar y configurar Fail2ban:**

```bash
sudo apt install -y fail2ban
sudo systemctl enable fail2ban --now
```

**4.3 — Crear filtro custom para Caddy** (`/etc/fail2ban/filter.d/caddy-status.conf`):
```ini
# Filtro para detectar errores 4xx en logs JSON de Caddy
[Definition]
# Caddy JSON log: {"request":{"remote_ip":"1.2.3.4",...},"status":4xx,...}
failregex = "remote_ip"\s*:\s*"<HOST>".*"status"\s*:\s*4[0-9]{2}
ignoreregex =
```

**4.4 — Crear filtro para bots** (`/etc/fail2ban/filter.d/caddy-botsearch.conf`):
```ini
# Filtro para detectar escaneo de rutas sospechosas en Caddy
[Definition]
failregex = "remote_ip"\s*:\s*"<HOST>".*"uri"\s*:\s*".*(?:wp-login|wp-admin|\.env|phpMyAdmin|/admin|\.git|\.php)"
ignoreregex =
```

**4.5 — Configurar jails** (`/etc/fail2ban/jail.local`):

```ini
[DEFAULT]
bantime.increment    = true
bantime.multiplier   = 2
bantime.maxtime      = 1w
bantime.overalljails = true
findtime             = 10m
maxretry             = 5
banaction            = iptables-multiport
backend              = auto
# Nunca banear IPs propias (loopback + rango Tailscale)
ignoreip             = 127.0.0.1/8 100.0.0.0/8

[sshd]
enabled  = true
maxretry = 3
bantime  = 24h

[caddy-status]
enabled  = true
port     = http,https
logpath  = /var/log/caddy/access.log
filter   = caddy-status
maxretry = 10

[caddy-botsearch]
enabled  = true
port     = http,https
logpath  = /var/log/caddy/access.log
filter   = caddy-botsearch
maxretry = 2
bantime  = 48h
```

```bash
sudo fail2ban-client reload
sudo fail2ban-client status   # verificar jails activos
```

**Criterio de éxito:** Tras peticiones maliciosas repetidas, la IP queda baneada con escalado 1h → 2h → 4h → ...

---

### FASE 5 — Cloudflare

**Objetivo:** Frontal público con WAF, ocultar IP de Oracle, forzar HTTPS y activar protecciones automáticas.

> **Recomendación:** Activar el proxy de Cloudflare lo antes posible para ocultar la IP de Oracle. Cada minuto con la IP expuesta es riesgo de indexación en Shodan/Censys.

**5.1 — DNS:**

- Registro A: `milo-jos.es` → `IP_ORACLE` → nube **naranja (Proxied)**
- Registro A: `www.milo-jos.es` → `IP_ORACLE` → nube **naranja (Proxied)**
- Verificación: `dig +short milo-jos.es` debe devolver IPs de Cloudflare, nunca la de Oracle

**5.2 — SSL/TLS:**

| Configuración | Valor |
| :-- | :-- |
| SSL/TLS Mode | **Full (strict)** |
| Always Use HTTPS | ON |
| HSTS | ON (empezar con max-age=15552000, 6 meses) |
| Minimum TLS Version | 1.2 |
| TLS 1.3 | ON |

Generar Origin Certificate (gratuito, 15 años):

- `SSL/TLS → Origin Server → Create Certificate`
- Guardar en VPS: `/etc/ssl/cloudflare/origin.pem` y `origin.key`
- Montar como volumen en el contenedor de Caddy en `compose.yaml`:
```yaml
caddy:
  volumes:
    - /etc/ssl/cloudflare:/etc/ssl/cloudflare:ro
```
- Referenciar en el `Caddyfile` con la directiva `tls`:
```
milo-jos.es {
    tls /etc/ssl/cloudflare/origin.pem /etc/ssl/cloudflare/origin.key
    reverse_proxy app:8000
}
```

**5.3 — WAF Custom Rules (5 disponibles en free):**

| \# | Condición | Acción |
| :-- | :-- | :-- |
| 1 | `cf.client.bot` AND NOT `Search Engine Crawlers` | Block |
| 2 | URI contiene `/admin` o `/login` AND país ≠ ES | Challenge |
| 3 | Geolocalización en países de alto riesgo para tu caso | Block |
| 4 | Rate limit: más de 100 req/min mismo origen | Block |
| 5 | User-Agent vacío | Block |

**5.4 — Configuraciones adicionales:**

```
Security → Settings    → Security Level: Medium
Security → Bots        → Bot Fight Mode: ON (gratis)
Security → WAF         → Managed Ruleset: ON (gratis desde 2024)
Speed    → Optimization → Auto Minify JS/CSS/HTML: ON
```

**Criterio de éxito:** `curl -H "Host: milo-jos.es" https://IP_ORACLE` = connection refused (iptables bloquea origen no-CF).

---

## 5. Checklist de Verificación Final

```bash
# ── Desde internet externo (móvil con datos o proxy) ──────────────
curl -v http://IP_ORACLE              # Esperado: timeout
curl -v https://IP_ORACLE             # Esperado: timeout
nmap -p 22,80,443 IP_ORACLE           # Esperado: todos filtered (22 por Oracle SL,
                                      #   80/443 por iptables — origen no es CF)
curl https://milo-jos.es              # Esperado: la web carga OK

# ── Desde tu máquina via Tailscale ────────────────────────────────
ssh usuario@100.x.y.z                 # Esperado: login OK
sudo fail2ban-client status           # Todas las jails activas
sudo iptables -L INPUT -n -v          # Reglas INPUT correctas
sudo iptables -L DOCKER-USER -n -v    # Reglas DOCKER-USER correctas
sudo ipset list cloudflare | wc -l    # Debe mostrar ~15 rangos
docker compose ps                     # Caddy + app healthy
```

---

## 6. Riesgos y Mitigaciones

| Riesgo | Prob. | Mitigación |
| :-- | :-- | :-- |
| Perder acceso SSH antes de restringir a Tailscale | Alta | Fase 1 es bloqueante — siempre verificar en segunda terminal |
| IP Oracle ya indexada en Shodan/histórico DNS | Media | Activar proxy CF lo antes posible; rotar IP en Oracle si ya está expuesta |
| IPs de Cloudflare desactualizadas en ipset | Baja | Cron semanal de actualización automática (incluido en Fase 3) |
| Banearse uno mismo con Fail2ban | Baja | `ignoreip = 100.0.0.0/8` cubre toda la subred Tailscale |
| Latencia extra por Tailscale DERP relay | Baja | Solo afecta al canal admin SSH, irrelevante para usuarios |
| Docker bypasea reglas INPUT | Alta | Reglas en cadena DOCKER-USER (incluido en Fase 3) |
| Logs de Caddy inaccesibles desde Fail2ban | Media | Volumen bind mount compartido entre contenedor y host |

---

## 7. Orden de Ejecución Definitivo

```
FASE 1 ✅     FASE 2        FASE 3          FASE 4       FASE 5
Tailscale  → Oracle FW  → iptables       → Fail2ban   → Cloudflare
(completada)  (red VCN)   (host + Docker)  (abuso)      (frontal)

Cada fase se verifica antes de pasar a la siguiente.
Nunca se cierra un vector de acceso sin tener el siguiente operativo.
```

---

## 8. Registro de Cambios del RFC

| Versión | Fecha | Cambios |
| :-- | :-- | :-- |
| 1.0 | 2026-03-26 | Versión inicial (generada por Perplexity) |
| 1.1 | 2026-03-26 | Revisión: Nginx → Caddy, añadido Docker/DOCKER-USER, Fail2ban adaptado a Caddy, rc.local → systemd, corregidos criterios de verificación, marcada Fase 1 como completada, actualizado diagrama de arquitectura |
