"""Configuración principal de Reflex para milo-jos.es (v2.0).

Lee variables de entorno desde .env y configura la app,
incluyendo fuentes self-hosted y hojas de estilo globales.
"""

import reflex as rx

config = rx.Config(
    app_name="milo_jos",
    # --- Frontend ---
    # Hojas de estilo: fuentes self-hosted + estilos globales
    # Los paths son relativos a assets/
    stylesheets=[
        "/fonts/fonts.css",
    ],
)
