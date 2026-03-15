# Changelog

Formato basado en [Semantic Versioning](https://semver.org/lang/es/).

## [2.0.0] - En desarrollo

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
- HTTPS automático con Let's Encrypt
- Deploy manual con `deploy.sh`

**Contenido:**
- Hero section con terminal animada
- Stack section con 4 capas técnicas
- Proyectos actualizados: Minerva, Ares, Proxmox Lab
- Bio profesional con timeline de carrera
- Sección de contacto directa

---

## [1.2.0] - 2024

- Versión original del portfolio
- 3 páginas: index, about_me, projects
- Desplegado en Vercel con export estático
- Paleta azul corporativo (Cerulean Blue + Picton Blue)
- Fuentes: Poppins + Comfortaa
