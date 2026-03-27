# Documentación — milo-jos.es v2.2.0

## Índice

| Documento | Descripción |
|---|---|
| [identity-system.md](identity-system.md) | Sistema de identidad: colores, tipografía, wordmark y assets |
| [architecture.md](architecture.md) | Arquitectura del sitio: navegación, componentes, secciones y estructura de archivos |
| [RFC-001: Infraestructura Segura.md](RFC-001:%20Infraestructura%20Segura.md) | Plan de seguridad: 4 capas (Cloudflare, Oracle SL, iptables/ipset, Fail2ban) |
| [CHANGELOG.md](CHANGELOG.md) | Historial de versiones |

> **Nota:** La documentación de despliegue (`manual-despliegue.md`) y especificaciones de
> infraestructura (`fase-5-deploy-stack.md`) están excluidas del repositorio por seguridad.
> Se encuentran solo en la máquina local dentro de `docs/`.

## Contexto del proyecto

**milo-jos.es** es el portfolio web personal de M1L0_J05, construido con
[Reflex](https://reflex.dev) (Python full-stack framework).

La versión 2.0 fue un rebrand completo. La versión actual (2.2.0) incluye:

- Nueva identidad visual (estética terminal/CLI, dark-first)
- Proyecto nuevo desde cero sobre Reflex 0.8.6 (v1.2 archivada en `milo-jos-v1/`)
- Migración de Vercel a VPS Oracle ARM con Docker + Caddy
- Arquitectura SPA híbrida con 5 secciones + rutas de detalle
- Infraestructura de seguridad en 4 capas (RFC-001)
- Carrusel horizontal de proyectos con scroll-snap

## Estructura del repositorio

```
m1l0-j05_WebSite/
├── milo-jos/          # Proyecto v2.2.0 (activo)
├── milo-jos-v1/       # Proyecto v1.2 (archivo, solo referencia)
└── docs/              # Documentación del proyecto
```

## Stack tecnológico

- **Framework:** Reflex 0.8.6 (Python 3.12+)
- **Hosting:** Oracle Cloud Free Tier ARM (4 OCPU, 24GB RAM)
- **Proxy reverso:** Caddy 2 (TLS con Cloudflare Origin Certificate)
- **Orquestación:** Docker Compose
- **CDN / WAF:** Cloudflare Free (proxy, DDoS, Bot Fight Mode)
- **Seguridad:** iptables/ipset (whitelist CF) + Fail2ban (jails Caddy + SSH)
- **Acceso admin:** Tailscale (SSH solo vía VPN mesh)
- **Fuentes:** JetBrains Mono, Outfit, Inter (self-hosted woff2)
- **CI/CD:** Deploy manual (`git pull` + `docker compose up -d --build`)
