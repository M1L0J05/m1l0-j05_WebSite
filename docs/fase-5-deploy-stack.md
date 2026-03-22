# Fase 5 — Stack de Deploy: Docker + Caddy + Oracle VPS

## Estado

> **Pendiente de implementación.** Los archivos `Dockerfile`, `compose.yaml`, `Caddyfile` y `deploy.sh` existen como placeholders vacíos en `milo-jos/`.

---

## Contexto y decisiones de diseño

| Aspecto | Decisión | Motivo |
|---------|----------|--------|
| Imagen base Python | `python:3.12-slim` | `pyproject.toml` exige `>=3.12`; imagen multi-arch (ARM64) |
| Gestión de deps | `uv sync --frozen --no-dev` | El proyecto usa `uv` con `uv.lock`; más rápido que pip |
| Build frontend | `reflex init` + `reflex export --no-zip` | Pre-compila Next.js en el stage de build para arranque rápido |
| Arquitectura | Full-stack (un contenedor) | v2 no tiene subdominio `api.`; Reflex sirve todo |
| Usuario runtime | No-root `reflex` (UID 1001) | Seguridad: mínimos privilegios |
| Reverse proxy | Caddy 2 (caddy:2-alpine) | HTTPS automático con Let's Encrypt sin configuración extra |
| Dominio en Caddyfile | Hardcodeado `milo-jos.es` | El dominio no cambia; más simple que env vars en Caddy |
| `milo-jos-v1/` | No tocar, no incluir en build | Código de referencia; queda fuera del build context (`milo-jos/`) |

---

## Rama de trabajo

```bash
git checkout -b feat/deploy-stack
```

---

## Archivos a implementar

### 1. `milo-jos/Dockerfile`

Multi-stage build. Stage `build` instala deps y pre-compila el frontend. Stage `runtime` es la imagen mínima que arranca en producción.

**Puntos críticos:**
- `unzip` + `curl` en el stage de build: Reflex los necesita para descargar `bun` (bundler interno del frontend).
- `reflex export --no-zip` en el stage de build genera los artefactos estáticos en `.web/`.
- En runtime solo se necesita `curl` (para el healthcheck de Docker Compose).
- `STOPSIGNAL SIGKILL`: Reflex 0.8.6 no propaga correctamente SIGTERM (igual que en v1).
- `EXPOSE 8000`: puerto interno de Reflex.

```dockerfile
# syntax=docker/dockerfile:1.7
# =============================================================================
# Dockerfile — Multi-stage, ARM64, Reflex full-stack
# =============================================================================

# --- Stage 1: Build ----------------------------------------------------------
FROM python:3.12-slim AS build

# Evitar prompts interactivos y no generar .pyc
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# uv: gestor de paquetes Python ultra-rápido
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Dependencias del sistema:
# - curl: descarga interna de Reflex
# - unzip: requerido por bun (bundler del frontend de Reflex)
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get install -y --no-install-recommends \
        curl unzip && \
    rm -rf /var/lib/apt/lists/*

# Instalar dependencias Python usando el lockfile (reproducible)
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Copiar código fuente y assets
COPY rxconfig.py ./
COPY milo_jos/ ./milo_jos/
COPY assets/ ./assets/

# Inicializar Reflex (genera .web/, descarga bun, instala node_modules)
# y pre-compilar el frontend Next.js para producción
RUN uv run reflex init && \
    uv run reflex export --no-zip

# --- Stage 2: Runtime --------------------------------------------------------
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# curl necesario únicamente para el healthcheck de Docker Compose
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Usuario no privilegiado para ejecutar la app
RUN groupadd --gid 1001 reflex && \
    useradd --uid 1001 --gid reflex --no-create-home --shell /bin/false reflex

# uv disponible en runtime para lanzar Reflex
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copiar solo los artefactos necesarios desde el stage de build
COPY --from=build /app/.venv       /app/.venv
COPY --from=build /app/milo_jos    /app/milo_jos
COPY --from=build /app/rxconfig.py /app/rxconfig.py
COPY --from=build /app/assets      /app/assets
COPY --from=build /app/.web        /app/.web
COPY pyproject.toml uv.lock ./

# El usuario reflex debe poseer todos los archivos
RUN chown -R reflex:reflex /app

USER reflex

# Reflex 0.8.6 no propaga SIGTERM correctamente en el backend
STOPSIGNAL SIGKILL

EXPOSE 8000

# Reflex full-stack: sirve frontend (Next.js) + backend (FastAPI) en :8000
CMD ["uv", "run", "reflex", "run", "--env", "prod"]
```

**Riesgo conocido:** Si `reflex export --no-zip` falla durante el build (por incompatibilidad de versión o entorno ARM64), eliminar esa línea y dejar solo `reflex init`. En ese caso, `reflex run --env prod` compilará el frontend en el primer arranque (más lento, pero funcional).

---

### 2. `milo-jos/compose.yaml`

Sin campo `version:` (deprecado en Compose V2).

```yaml
# compose.yaml — Orquestación Docker (Caddy + Reflex)

services:
  caddy:
    image: caddy:2-alpine
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
      - "443:443/udp"   # HTTP/3
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

**Nota sobre `start_period`:** Reflex tarda en inicializar el frontend. Si el healthcheck falla consistentemente en el primer arranque, aumentar a `60s` o `90s`.

---

### 3. `milo-jos/Caddyfile`

```
# Caddyfile — Reverse proxy + HTTPS automático

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

---

### 4. `milo-jos/deploy.sh`

Hacer ejecutable tras escribirlo: `chmod +x deploy.sh`

```bash
#!/bin/bash
# deploy.sh — Script de despliegue manual para Oracle VPS
# Uso: ./deploy.sh [--build] [--restart]
#   --build    Reconstruye la imagen Docker sin caché antes de levantar
#   --restart  Reinicia los contenedores existentes sin recrearlos

set -euo pipefail

PROJECT_DIR="/opt/milo-jos/milo-jos"

echo "==> Actualizando código..."
git -C "$PROJECT_DIR" pull origin main

if [[ "${1:-}" == "--build" ]]; then
    echo "==> Reconstruyendo imagen..."
    docker compose -f "$PROJECT_DIR/compose.yaml" build --no-cache
fi

if [[ "${1:-}" == "--restart" ]]; then
    echo "==> Reiniciando servicios (sin recrear)..."
    docker compose -f "$PROJECT_DIR/compose.yaml" restart
else
    echo "==> Levantando servicios..."
    docker compose -f "$PROJECT_DIR/compose.yaml" up -d
fi

echo "==> Verificando salud..."
sleep 10
docker compose -f "$PROJECT_DIR/compose.yaml" ps
curl -sf https://milo-jos.es > /dev/null && echo "OK: Sitio accesible" || echo "ERROR: Sitio no responde"
```

---

### 5. `milo-jos/milo_jos/version.py`

```python
__version__: str = "2.2.0"
```

---

### 6. `milo-jos/CHANGELOG.md` — entrada nueva

Insertar al inicio (encima de `[2.1.0]`):

```markdown
## [2.2.0] — 2026-03-21

### Añadido

- **Dockerfile** multi-stage ARM64: stage `build` con `python:3.12-slim` + `uv` + `reflex init/export`; stage `runtime` con usuario no-root `reflex` (UID 1001).
- **compose.yaml**: orquestación con servicios `caddy` (reverse proxy HTTPS) y `app` (Reflex full-stack), healthcheck integrado vía `/ping`.
- **Caddyfile**: HTTPS automático (Let's Encrypt), headers de seguridad (HSTS, X-Frame-Options, Referrer-Policy), compresión gzip/zstd, redirect www → non-www.
- **deploy.sh**: script de despliegue manual con flags `--build` (rebuild sin caché) y `--restart` (reinicio rápido sin recrear).

### Modificado

- `milo_jos/version.py`: bump `2.1.0` → `2.2.0`.
```

---

## Secuencia de commits

```
feat: implementar Dockerfile multi-stage para Reflex ARM64
feat: configurar compose.yaml con Caddy + Reflex
feat: configurar Caddyfile con HTTPS y headers de seguridad
feat: implementar script de despliegue deploy.sh
chore: bump versión a 2.2.0 y actualizar CHANGELOG
```

---

## Verificación post-implementación

```bash
# Validar compose.yaml
docker compose config

# Build local (desde milo-jos/)
docker build -f Dockerfile -t milo-jos:test .

# Arrancar y comprobar healthcheck
docker run --rm -p 8000:8000 -e REFLEX_ENV=prod milo-jos:test
curl localhost:8000/ping

# Levantar stack completo
docker compose up -d
docker compose ps

# Permisos deploy.sh
ls -la deploy.sh  # debe mostrar -rwxr-xr-x

# Tests existentes (no deben romperse)
cd milo-jos && pytest tests/
```

---

## Checklist pre-launch (VPS)

- [ ] DNS `milo-jos.es` apunta a IP del VPS (`dig milo-jos.es`)
- [ ] Puertos 80 y 443 abiertos (Oracle Security Lists + iptables)
- [ ] `.env` creado desde `.env.example` con `REFLEX_ENV=prod`
- [ ] `docker compose up -d --build` sin errores
- [ ] HTTPS funcionando (`curl -I https://milo-jos.es`)
- [ ] Certificado SSL válido
- [ ] Redirect `www.milo-jos.es` → `milo-jos.es` funcionando

---

## Referencia cruzada

- Especificaciones de `compose.yaml`, `Caddyfile` y `deploy.sh`: [`docs/deployment.md`](deployment.md)
- Código de referencia v1 (no tocar): `milo-jos-v1/Dockerfile`, `milo-jos-v1/front_build.sh`
- Plan global de fases: [`docs/plan-rebrand-v2.md`](plan-rebrand-v2.md)
