"""Paquete de secciones — milo-jos.es v2.0.

Re-exporta todas las funciones de sección para composición en páginas:

    from milo_jos.sections import hero_section, stack_section
"""

from .about_me import about_me_section
from .contact import contact_section
from .hero import hero_section
from .projects import projects_section
from .stack import stack_section

__all__: list[str] = [
    "about_me_section",
    "contact_section",
    "hero_section",
    "projects_section",
    "stack_section",
]
