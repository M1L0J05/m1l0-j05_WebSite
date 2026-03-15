# Guía de Despliegue — Oracle VPS ARM

## Arquitectura

```
Oracle VPS ARM (4 cores, 24GB RAM)
│
├── Docker Engine
│   ├── caddy (puertos 80, 443)
│   │   ├── milo-jos.es → proxy → app:8000
│   │   └── TLS automático (Let's Encrypt)
│   │
│   └── app (Reflex full-stack)
│       ├── Frontend (Next.js servido por Reflex)
│       └── Backend (FastAPI bajo Reflex)
│
├── /opt/milo-jos/
│   ├── compose.yaml
│   ├── .env
│   └── Caddyfile
│
└── Firewall
    ├── 80/tcp  → HTTP (redirect a HTTPS)
    ├── 443/tcp → HTTPS
    └── 22/tcp  → SSH (restringido por IP)
```

**Dominio único:** `milo-jos.es` (sin subdominio `api.`)

---

## Requisitos previos

- VPS Oracle Free Tier ARM (Ampere A1, 4 OCPU, 24GB RAM)
- Ubuntu 22.04+ ARM64
- Dominio `milo-jos.es` con acceso a DNS
- Acceso SSH al VPS

---

## 1. Setup inicial del VPS

### Instalar Docker

```bash
# Instalar Docker Engine (ARM64)
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
# Cerrar sesión y volver a entrar para aplicar grupo

# Verificar
docker --version
docker compose version
```

### Configurar firewall

```bash
# Oracle Security Lists (en la consola web de Oracle Cloud):
# - Ingress rule: 0.0.0.0/0 TCP 80
# - Ingress rule: 0.0.0.0/0 TCP 443
# - Ingress rule: TU_IP/32 TCP 22

# En el VPS (iptables de Oracle Linux / Ubuntu):
sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 80 -j ACCEPT
sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 443 -j ACCEPT
sudo netfilter-persistent save
```

### Configurar DNS

Crear registro A en el proveedor de dominio:

| Tipo | Nombre | Valor | TTL |
|---|---|---|---|
| A | `@` | `<IP_PUBLICA_VPS>` | 300 |
| A | `www` | `<IP_PUBLICA_VPS>` | 300 |

---

## 2. Archivos de despliegue

### compose.yaml

```yaml
services:
  caddy:
    image: caddy:2-alpine
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
      - "443:443/udp"  # HTTP/3
    volumes:
      - ./Caddyfile:/etc/caddy/Caddyfile:ro
      - caddy_data:/data
      - caddy_config:/config
    depends_on:
      app:
        condition: service_healthy
    networks:
      - web

  app:
    build:
      context: .
      dockerfile: Dockerfile
    restart: unless-stopped
    env_file: .env
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/ping"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    networks:
      - web

volumes:
  caddy_data:
  caddy_config:

networks:
  web:
    driver: bridge
```

### Caddyfile

```
milo-jos.es {
    reverse_proxy app:8000

    header {
        X-Content-Type-Options nosniff
        X-Frame-Options DENY
        Referrer-Policy strict-origin-when-cross-origin
        Strict-Transport-Security "max-age=31536000; includeSubDomains"
    }

    encode gzip zstd
}

www.milo-jos.es {
    redir https://milo-jos.es{uri} permanent
}
```

### .env.example

```bash
# Dominio de producción
DOMAIN=milo-jos.es

# Entorno Reflex
REFLEX_ENV=prod
```

### Dockerfile (resumen)

- **Stage 1 (build):** `python:3.11-slim`, instala deps, `reflex init`
- **Stage 2 (prod):** Copia artefactos, usuario no-root `reflex`
- **CMD:** `reflex run --env prod` (full-stack)
- Compatible ARM64 (las imágenes `python:3.11-slim` son multi-arch)

> El Dockerfile completo se genera en la Fase 5 de implementación.

---

## 3. Deploy

### Primer despliegue

```bash
# En el VPS
cd /opt
sudo git clone <REPO_URL> milo-jos
cd milo-jos/milo-jos
cp .env.example .env
# Editar .env con valores de producción

docker compose up -d --build
# Caddy obtiene certificado SSL automáticamente
```

### deploy.sh (actualizaciones posteriores)

```bash
#!/bin/bash
# Script de deploy para milo-jos.es
# Uso: ./deploy.sh [--build] [--restart]

set -euo pipefail

PROJECT_DIR="/opt/milo-jos/milo-jos"

echo "==> Actualizando código..."
git -C "$PROJECT_DIR" pull origin main

if [[ "${1:-}" == "--build" ]]; then
    echo "==> Reconstruyendo imagen..."
    docker compose -f "$PROJECT_DIR/compose.yaml" build --no-cache
fi

echo "==> Reiniciando servicios..."
docker compose -f "$PROJECT_DIR/compose.yaml" up -d

echo "==> Verificando salud..."
sleep 10
docker compose -f "$PROJECT_DIR/compose.yaml" ps
curl -sf https://milo-jos.es > /dev/null && echo "OK: Sitio accesible" || echo "ERROR: Sitio no responde"
```

---

## 4. Operaciones comunes

| Operación | Comando |
|---|---|
| Ver logs | `docker compose logs -f` |
| Solo logs app | `docker compose logs -f app` |
| Reiniciar | `docker compose restart` |
| Rebuild | `docker compose up -d --build` |
| Parar todo | `docker compose down` |
| Ver estado | `docker compose ps` |
| Certificados Caddy | Automáticos, sin intervención |

---

## 5. Checklist pre-launch

- [ ] DNS apuntando a IP del VPS (verificar con `dig milo-jos.es`)
- [ ] Puertos 80 y 443 abiertos (Oracle Security Lists + iptables)
- [ ] `.env` configurado con valores de producción
- [ ] `docker compose up -d --build` sin errores
- [ ] HTTPS funcionando (`curl -I https://milo-jos.es`)
- [ ] Certificado SSL válido
- [ ] Redirect www → sin www funcionando

---

## 6. Desmontar Vercel (instrucciones)

1. **Vercel Dashboard:** [vercel.com/dashboard](https://vercel.com/dashboard)
   - Seleccionar proyecto → Settings → General → "Delete Project"
   - Si hay dominio custom: Settings → Domains → Remove primero

2. **GitHub Actions:** Repo → Settings → Actions → General → "Disable Actions"

3. **Integración Vercel-GitHub:**
   - GitHub → Settings (perfil) → Applications → Buscar "Vercel" → Revoke
   - GitHub → Settings → Integrations → Buscar "Vercel" → Remove

4. **DNS:** Eliminar cualquier registro CNAME que apunte a `cname.vercel-dns.com`
