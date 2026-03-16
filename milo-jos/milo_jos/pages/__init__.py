"""Paquete de páginas — milo-jos.es v2.0.

Re-exporta las funciones de página para registro en la app:

    from milo_jos.pages import index, project_detail
"""

from .index import index
from .project_detail import project_detail

__all__: list[str] = [
    "index",
    "project_detail",
]
