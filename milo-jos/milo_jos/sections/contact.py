"""Sección Contacto — Email directo + redes + disponibilidad.

Diseño minimalista centrado con badge de disponibilidad,
llamada a la acción principal por email y enlaces a redes sociales.

Especificaciones: docs/architecture.md > Secciones > Contacto
"""

import reflex as rx

from milo_jos.styles import (
    Color,
    FontFamily,
    FontSize,
    FontWeight,
    GlassBg,
    HEADING_STYLE,
    LABEL_STYLE,
    SECTION_PADDING,
    SECTION_REVEAL,
    CONTAINER_MAX_WIDTH,
)
from milo_jos.utils.constants import (
    EMAIL,
    AVAILABILITY_BADGE,
    SOCIAL_LINKS,
)
from milo_jos.components import badge, primary_button


def _availability_badge() -> rx.Component:
    """Badge verde indicando disponibilidad para proyectos freelance.

    Returns:
        Componente badge con estado de disponibilidad.
    """
    return badge(
        AVAILABILITY_BADGE,
        color=Color.ACCENT_GREEN,
        bg="rgba(63, 185, 80, 0.1)",
        border_color="rgba(63, 185, 80, 0.3)",
    )


def _social_link(social: dict[str, str]) -> rx.Component:
    """Enlace a red social con icono y efecto hover.

    Args:
        social: Diccionario con keys 'name', 'url' e 'icon'.

    Returns:
        Componente link con icono de la red social.
    """
    return rx.link(
        rx.icon(
            tag=social["icon"],
            size=24,
            color=Color.TEXT_SECONDARY,
            _hover={"color": Color.ACCENT_CYAN},
            transition="color 0.2s ease",
        ),
        href=social["url"],
        target="_blank",
        title=social["name"],
    )


def _social_links_row() -> rx.Component:
    """Fila horizontal con iconos de todas las redes sociales.

    Returns:
        Componente hstack con los enlaces sociales.
    """
    return rx.hstack(
        *[_social_link(social) for social in SOCIAL_LINKS],
        spacing="5",
        justify="center",
    )


def contact_section() -> rx.Component:
    """Sección completa de Contacto del portfolio.

    Layout centrado y minimalista con badge de disponibilidad,
    texto principal, subtítulo, botón CTA de email,
    enlaces a redes sociales y nota de tiempo de respuesta.

    Returns:
        Sección Contacto lista para componer en la página principal.
    """
    return rx.box(
        rx.vstack(
            # Encabezado de sección
            rx.heading(
                "Contacto",
                **HEADING_STYLE,
                font_size=["1.75rem", "2rem", "2.25rem"],
                as_="h1",
            ),
            # Badge de disponibilidad
            _availability_badge(),
            # Pregunta principal
            rx.heading(
                "¿Tienes un proyecto en mente?",
                font_family=FontFamily.HEADING,
                font_size=["1.25rem", "1.5rem", "1.75rem"],
                font_weight=FontWeight.BOLD,
                color=Color.TEXT_PRIMARY,
                as_="h2",
            ),
            # Subtítulo
            rx.text(
                "Escríbeme directamente — sin formularios, sin esperas.",
                color=Color.TEXT_SECONDARY,
                font_size=FontSize.BODY,
            ),
            # Botón CTA de email
            primary_button(
                EMAIL,
                href=f"mailto:{EMAIL}",
            ),
            # Enlaces a redes sociales
            _social_links_row(),
            # Nota de tiempo de respuesta
            rx.text(
                "Respondo en menos de 24h",
                **LABEL_STYLE,
            ),
            spacing="5",
            align="center",
            text_align="center",
            max_width=CONTAINER_MAX_WIDTH,
            width="100%",
            margin_x="auto",
        ),
        id="contacto",
        as_="section",
        width="100%",
        **SECTION_PADDING,
        **SECTION_REVEAL,
    )
