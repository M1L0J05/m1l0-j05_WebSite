# Plan de Rebrand v2.0

## Decisiones clave

| Aspecto | Decisión |
|---|---|
| Navegación | Híbrida: SPA con anclas (#hero, #stack, etc.) + rutas `/proyectos/:id` |
| Framework | Proyecto nuevo desde cero sobre Reflex 0.8.6 |
| Código v1.2 | Archivado en `milo-jos-v1/` como referencia (se elimina tras launch) |
| Fuentes | Self-hosted (woff2) por GDPR compliance |
| Hero background | CSS-only con gradientes animados |
| Imágenes proyectos | Placeholders iniciales |
| Hosting | Oracle Free Tier ARM (4 cores, 24GB) |
| Arquitectura deploy | Reflex full-stack (un contenedor) + Caddy |
| CI/CD | Manual con `deploy.sh` |
| Dominio | Solo `milo-jos.es` (eliminar subdominio `api.`) |

---

## Fase 0 — Setup y Limpieza (2-3 días)

### Limpieza Vercel / GitHub Actions — COMPLETADO

1. ~~**Vercel:** Dashboard → proyecto → Settings → Delete Project~~
2. ~~**GitHub Actions:** Repo → Settings → Actions → Disable Actions~~
3. ~~**Integración:** GitHub Settings → Applications → Revocar acceso Vercel~~

### Setup del repositorio

| Tarea | Prioridad | Estado |
|---|---|---|
| Archivar código v1 en `milo-jos-v1/` | Alta | Completado |
| Crear scaffolding `milo-jos/` nuevo (Reflex 0.8.6) | Alta | Completado |
| `requirements.txt` → `reflex==0.8.6` | Alta | Completado |
| `rxconfig.py` compatible 0.8.6, importar version | Alta | Completado |
| `version.py` → `__version__ = "2.0.0"` | Alta | Completado |
| `.env.example` con variables documentadas | Media | Completado |
| Crear estructura `tests/` con `conftest.py` | Media | Completado |

---

## Fase 1 — Identidad Visual (2-3 días)

| Tarea | Archivo | Estado |
|---|---|---|
| Reescribir paleta de colores (10 tokens) | `styles/colors.py` | Completado |
| Reescribir tipografía (3 familias, escala rem) | `styles/fonts.py` | Completado |
| Descargar fuentes woff2 + fonts.css | `assets/fonts/` | Completado |
| Reescribir estilos base + glassmorphism + breakpoints | `styles/styles.py` | Completado |
| Implementar animaciones CSS (keyframes) | `styles/animations.py` | Completado |
| Implementar constantes de app | `utils/constants.py` | Completado |
| Generar favicon "M1" (16, 32, 180, 512) | `assets/favicon.ico` | Pendiente |
| Crear OG image placeholder (1200x630) | `assets/images/root/og-image.png` | Pendiente |

> Detalle completo de tokens en [identity-system.md](identity-system.md)

---

## Fase 2 — Componentes UI (3-4 días)

| Componente | Archivo | Descripción | Estado |
|---|---|---|---|
| Navbar | `components/navbar.py` | Sticky, glassmorphism, wordmark, drawer mobile | Completado |
| Footer | `components/footer.py` | Minimalista, version dinámica desde `version.py` | Completado |
| Badge | `components/badge.py` | Tags tecnología, monospace, cian | Completado |
| Button | `components/button.py` | Primario (CTA) + Secundario (outline) | Completado |
| Card | `components/card.py` | Glassmorphism, hover glow + translateY(-4px) | Completado |
| Timeline | `components/timeline.py` | Línea vertical, dots con glow pulsante | Completado |
| Terminal | `components/terminal.py` | Bloque terminal, typewriter CSS | Completado |
| Template | `templates/template.py` | Layout base SPA: navbar + secciones + footer | Completado |

**Eliminar:** `components/quote.py` (reemplazado por el nuevo diseño)

---

## Fase 3 — Secciones y Contenido (5-6 días)

| Sección | ID ancla | Contenido clave |
|---|---|---|
| Hero | `#hero` | Wordmark con cursor blink, terminal `whoami`, 2 CTAs, gradiente CSS |
| Stack | `#stack` | 4 capas (Frontend/Backend/Infra/Automation), badges tech |
| Proyectos | `#proyectos` | Cards con estado (PROD/LAB/DEV), Minerva, Ares, Proxmox, slot "coming soon" |
| Sobre Mí | `#sobre-mi` | Bio profesional + timeline 2023-2026 |
| Contacto | `#contacto` | Email directo, links sociales, badge disponibilidad |

**Archivos adicionales:**
- Actualizar `assets/data/projects.json` con nuevos proyectos
- Crear `pages/project_detail.py` (ruta dinámica `/proyectos/:id`)
- Reescribir `milo_jos.py` (punto de entrada SPA)

---

## Fase 4 — Animaciones y Responsive (3-4 días)

| Animación | Duración | Elemento |
|---|---|---|
| Cursor blink (`step-end`) | 1s infinite | Wordmark `█` |
| Typewriter | 60ms/char | Terminal hero |
| Glow hover | 300ms ease | Cards proyecto |
| Timeline pulse | 2s infinite | Dot activo (presente) |
| Scroll reveal (fade-in + translateY) | 500ms ease-out | Todas las secciones |
| Gradiente animado | continuo | Fondo hero |

**Reglas:**
- Solo propiedades GPU: `transform`, `opacity`
- `prefers-reduced-motion`: desactivar todas
- Máximo 3 animaciones simultáneas
- Fallback glassmorphism si no hay `backdrop-filter`
- Responsive: 320px / 768px / 1024px / 1440px

---

## Fase 5 — Docker + Caddy + Oracle VPS (3-4 días)

| Tarea | Archivo |
|---|---|
| Dockerfile multi-stage ARM64 (python:3.11-slim) | `Dockerfile` |
| Caddyfile (reverse proxy, HTTPS, headers seguridad) | `Caddyfile` |
| Docker Compose (caddy + app, red bridge, healthcheck) | `compose.yaml` |
| Script de deploy (git pull + compose up) | `deploy.sh` |
| Variables de entorno documentadas | `.env.example` |
| Actualizar `.dockerignore` | `.dockerignore` |

> Guía completa de despliegue en [deployment.md](deployment.md)

---

## Fase 6 — SEO, Tests, Docs y Launch (3-4 días)

| Tarea | Detalle |
|---|---|
| Meta tags | Title, description, OG protocol, Twitter cards |
| Schema.org | Structured data `Person` (JSON-LD) |
| Sitemap + robots.txt | Regenerar para nueva estructura |
| Tests pytest | Renderización secciones + datos projects.json |
| Docstrings español | Todas las funciones y clases |
| Documentación por módulo | styles, components, sections |
| Lighthouse | Performance, Accessibility, SEO > 90 |

---

## Estimación total

| Fase | Días |
|---|---|
| 0 — Setup y limpieza | 2-3 |
| 1 — Identidad visual | 2-3 |
| 2 — Componentes UI | 3-4 |
| 3 — Contenido y secciones | 5-6 |
| 4 — Animaciones y responsive | 3-4 |
| 5 — Docker + Caddy + VPS | 3-4 |
| 6 — SEO, tests, docs, launch | 3-4 |
| **Total** | **21-28 días** |
