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

# uv: gestor de paquetes Python ultra-rápido con soporte de lockfile
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Dependencias del sistema:
# - curl: descarga interna de Reflex durante init
# - unzip: requerido por bun (bundler del frontend de Reflex)
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && apt-get install -y --no-install-recommends \
        curl unzip && \
    rm -rf /var/lib/apt/lists/*

# Instalar dependencias Python usando lockfile (reproducible, sin red innecesaria)
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Copiar código fuente y assets estáticos
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

# El usuario reflex debe poseer todos los archivos de la app
RUN chown -R reflex:reflex /app

USER reflex

# Reflex 0.8.6 no propaga SIGTERM correctamente en el backend
STOPSIGNAL SIGKILL

EXPOSE 8000

# Reflex full-stack: sirve frontend (Next.js) + backend (FastAPI) en :8000
CMD ["uv", "run", "reflex", "run", "--env", "prod"]
