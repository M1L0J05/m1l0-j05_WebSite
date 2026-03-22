# Changelog

Todos los cambios notables de este proyecto se documentan en este archivo.
Formato basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).
Versiones según [Semantic Versioning](https://semver.org/lang/es/).

---

## [2.2.0] — 2026-03-22

### Añadido

- **Dockerfile** multi-stage ARM64: stage `build` con `python:3.12-slim` + `uv` + `reflex init/export`; stage `runtime` con usuario no-root `reflex` (UID 1001).
- **compose.yaml**: orquestación con servicios `caddy` (reverse proxy HTTPS) y `app` (Reflex full-stack), healthcheck integrado vía `/ping`. El servicio `app` usa `image:` — la imagen se carga vía `docker load`, sin repo en el VPS.
- **Caddyfile**: HTTPS automático (Let's Encrypt), headers de seguridad (HSTS, X-Frame-Options, Referrer-Policy), compresión gzip/zstd, redirect www → non-www.
- **deploy.sh**: script ejecutado desde máquina local con subcomandos `build` (buildx ARM64 + save), `push` (scp vía Tailscale + docker load + compose up), `all` y `sync` (actualiza archivos de config en VPS).

### Modificado

- `milo_jos/version.py`: bump `2.1.0` → `2.2.0`.
- `.env.example`: renombrada `DEPLOY_HOST` → `VPS_HOST` (IP Tailscale); comentarios actualizados.

---

## [2.1.0] — 2026-03-21

### Añadido

- **Carrusel horizontal de proyectos**: la sección `#proyectos` del index pasa de un grid multi-fila a un carrusel de una sola fila con scroll-snap CSS, eliminando el scroll vertical excesivo.
- **`CarouselState`** (`milo_jos/states/carousel_state.py`): nuevo estado Reflex que gestiona el índice activo del carrusel y coordina scroll programático vía `rx.call_script`.
- **Flechas de navegación**: botones `chevron_left`/`chevron_right` posicionados absolutamente, visibles en tablet y desktop. Ocultos en mobile (swipe táctil).
- **Dots indicadores de posición**: fila de puntos clicables debajo del carrusel que reflejan el card activo mediante `CarouselState.active_index`.
- **Gradientes de borde**: hints visuales que indican contenido oculto a izquierda y derecha.
- **CSS scrollbar-hide**: regla global `.carousel-scroll-container` añadida en `animations.py` para ocultar la scrollbar nativa en todos los navegadores.

### Modificado

- `milo_jos/sections/projects.py`: reemplazado `rx.grid` por estructura de carrusel con helpers `_card_wrapper`, `_nav_button`, `_edge_fade`, `_dot_indicator`, `_dot_indicators`.
- `milo_jos/styles/animations.py`: añadida constante `CAROUSEL_SCROLLBAR_HIDE` e incluida en `get_all_keyframes()`.
- `milo_jos/version.py`: bump `2.0.0` → `2.1.0`.

---

## [2.0.0] — 2026-03-01

### Notas

Versión inicial del portfolio con secciones hero, stack, proyectos (grid), sobre mí y contacto.
