# Changelog

Formato basado en [Semantic Versioning](https://semver.org/lang/es/).
Para cambios detallados por versión, ver también `milo-jos/CHANGELOG.md`.

---

## [2.2.0] — 2026-03-27

### Infraestructura y despliegue

- **Dockerfile** multi-stage ARM64 con `uv` + usuario no-root `reflex` (UID 1001)
- **compose.yaml** con Caddy (reverse proxy) + Reflex app + healthcheck vía `/ping`
- **Caddyfile** con TLS Cloudflare Origin Certificate (Full Strict), headers de seguridad, logging JSON para Fail2ban
- **deploy.sh** con flags `--build` y `--restart` para actualizaciones en el VPS
- **Seguridad (RFC-001):** 4 capas implementadas — Cloudflare WAF, Oracle Security List, iptables/ipset con whitelist Cloudflare + DOCKER-USER, Fail2ban con jails progresivas
- Scripts de infraestructura: `deploy-to-vps.sh` (setup inicial), `setup-fail2ban.sh`

---

## [2.1.0] — 2026-03-21

### Carrusel de proyectos

- Carrusel horizontal con scroll-snap CSS (reemplaza grid multi-fila)
- `CarouselState` para gestión de índice activo y scroll programático
- Flechas de navegación (tablet/desktop) + dots indicadores
- Gradientes de borde y scrollbar oculta

---

## [2.0.0] — 2026-03-01

### BREAKING CHANGE: Rebrand completo

**Identidad:**
- Nueva paleta de colores dark-first (cian #00B4D8 + naranja #FF6B2B)
- Nueva tipografía: JetBrains Mono (display/code), Outfit (headings), Inter (body)
- Wordmark tipográfico `>_ M1L0_J05` con estética terminal

**Arquitectura:**
- Migración de Reflex 0.4.4 a 0.8.6
- SPA híbrida: 5 secciones por ancla + rutas `/proyectos/:id`
- Nuevos componentes UI: Badge, Button, Card, Timeline, Terminal
- Sistema glassmorphism en cards y navbar

**Infraestructura:**
- Migración de Vercel a Oracle Cloud VPS ARM
- Docker multi-stage + Caddy como reverse proxy

**Contenido:**
- Hero section con terminal animada
- Stack section con 4 capas técnicas
- Proyectos actualizados: Minerva, Ares, Proxmox Lab
- Bio profesional con timeline de carrera
- Sección de contacto directa

---

## [1.2.0] — 2024

- Versión original del portfolio
- 3 páginas: index, about_me, projects
- Desplegado en Vercel con export estático
- Paleta azul corporativo (Cerulean Blue + Picton Blue)
- Fuentes: Poppins + Comfortaa
