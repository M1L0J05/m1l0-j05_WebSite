"""Página principal (SPA) — milo-jos.es v2.0.

Compone todas las secciones del portfolio en una sola página
con anclas para navegación interna. Envuelta en el template base.

Ruta: /
"""

import reflex as rx

from milo_jos.templates import template
from milo_jos.sections import (
    hero_section,
    stack_section,
    projects_section,
    about_me_section,
    contact_section,
)
from milo_jos.utils.constants import META_TITLE, META_DESCRIPTION


def index() -> rx.Component:
    """Página index — SPA con todas las secciones del portfolio.

    Orden de secciones:
    1. Hero (#hero) — viewport completo
    2. Stack Técnico (#stack)
    3. Proyectos (#proyectos)
    4. Sobre Mí (#sobre-mi)
    5. Contacto (#contacto)

    Returns:
        Layout completo con navbar + secciones + footer.
    """
    return template(
        rx.fragment(
            hero_section(),
            stack_section(),
            projects_section(),
            about_me_section(),
            contact_section(),
        )
    )
