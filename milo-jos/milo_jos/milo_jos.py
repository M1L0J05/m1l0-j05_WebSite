"""Punto de entrada de la aplicación Reflex — milo-jos.es v2.0.

Crea la instancia de rx.App con los estilos globales y registra
las páginas disponibles:
- / (index SPA con todas las secciones)
- /proyectos/[id] (detalle de proyecto, ruta dinámica)
"""

import reflex as rx

from milo_jos.styles import BASE_STYLE
from milo_jos.pages.index import index
from milo_jos.pages.project_detail import project_detail
from milo_jos.utils.constants import META_TITLE, META_DESCRIPTION


app = rx.App(style=BASE_STYLE)

# Página principal — SPA con anclas
app.add_page(
    index,
    route="/",
    title=META_TITLE,
    description=META_DESCRIPTION,
)

# Detalle de proyecto — Ruta dinámica
# El segmento [id] se inyecta automáticamente en rx.State.id
app.add_page(
    project_detail,
    route="/proyectos/[id]",
    title=META_TITLE,
)
