# Se utiliza la imagen base de Python 3.11
FROM python:3.11

# Copiar el contexto local al directorio `/app` dentro del contenedor (ver .dockerignore)
WORKDIR /app
COPY . .

# Instalar los requisitos de la aplicación y Reflex en el contenedor
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Crear un usuario no privilegiado para ejecutar la aplicación
RUN groupadd -r reflex && useradd -r -g reflex reflex && \
    chown -R reflex:reflex /app

# Inicializar las plantillas y preparar la aplicación
RUN reflex init

# Necesario hasta que Reflex pase adecuadamente SIGTERM en el backend.
STOPSIGNAL SIGKILL

# Siempre aplicar migraciones antes de iniciar el backend.
CMD reflex run --env prod --backend-only
