# Documentación — milo-jos.es v2.0

## Índice

| Documento | Descripción |
|---|---|
| [plan-rebrand-v2.md](plan-rebrand-v2.md) | Plan maestro del rebrand: fases, tareas, decisiones y estimaciones |
| [identity-system.md](identity-system.md) | Sistema de identidad: colores, tipografía, wordmark y assets |
| [architecture.md](architecture.md) | Arquitectura del sitio: navegación, componentes, secciones y estructura de archivos |
| [deployment.md](deployment.md) | Guía de despliegue: Oracle VPS ARM + Docker + Caddy |
| [CHANGELOG.md](CHANGELOG.md) | Historial de versiones |

## Contexto del proyecto

**milo-jos.es** es el portfolio web personal de M1L0_J05, construido con
[Reflex](https://reflex.dev) (Python full-stack framework).

La versión 2.0 es un rebrand completo que incluye:

- Nueva identidad visual (estética terminal/CLI, dark-first)
- Reescritura sobre Reflex 0.8.6 (desde 0.4.4)
- Migración de Vercel a VPS Oracle ARM con Docker + Caddy
- Arquitectura SPA híbrida con 5 secciones + rutas de detalle

## Stack tecnológico v2.0

- **Framework:** Reflex 0.8.6 (Python)
- **Hosting:** Oracle Cloud Free Tier ARM (4 cores, 24GB RAM)
- **Proxy reverso:** Caddy (HTTPS automático)
- **Orquestación:** Docker Compose
- **Fuentes:** JetBrains Mono, Outfit, Inter (self-hosted)
- **CI/CD:** Deploy manual con script (`deploy.sh`)
