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
