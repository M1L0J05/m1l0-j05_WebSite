"""Sección Sobre Mí — Bio profesional + timeline de carrera.

Diseño en dos columnas (desktop) con bio a la izquierda
y línea temporal a la derecha. En móvil colapsa a una sola columna.

Especificaciones: docs/architecture.md > Secciones > Sobre Mí
"""

import reflex as rx

from milo_jos.styles import (
    Color,
    FontFamily,
    FontSize,
    FontWeight,
    HEADING_STYLE,
    SECTION_PADDING,
    SECTION_REVEAL,
    CONTAINER_MAX_WIDTH,
)
from milo_jos.utils.constants import TAGLINE_BIO, UVP
from milo_jos.components import timeline, timeline_item


# --- Datos del timeline profesional ---

_TIMELINE_ITEMS: list[dict] = [
    {
        "year": "2013",
        "title": "Inicio en equipo OSINT",
        "description": (
            "Primeros proyectos con Python y JavaScript. "
            "Fundamentos de programación."
        ),
        "is_active": False,
    },
    {
        "year": "2016",
        "title": "Inicio en equipo de Obtención",
        "description": (
            "Periodo de maduración y crecimiento. "
            "Inicio del Proyecto Ares."
        ),
        "is_active": False,
    },
    {
        "year": "2020",
        "title": "Inicio en equipo IT / ID+i",
        "description": (
            "Presento Ares y accedo al erquipo. "
            "Desarrollo de aplicaciones y matenimeinto de infraestructura."
        ),
        "is_active": False,
    },
    {
        "year": "2024",
        "title": "Full-Stack & DevOps",
        "description": (
            "Transición a infraestructura. Docker, SysAdmin, CI/CD. "
            "Proyectos propios en producción."
        ),
        "is_active": False,
    },
    {
        "year": "2025",
        "title": "Infraestructura & Automatización",
        "description": (
            "Transición y puesta en produccion de ecosistema Proxmox. "
            "Pipelines de automatización y continuo desarrollo de herramientas y aplicaciones."
        ),
        "is_active": False,
    },
    {
        "year": "2026",
        "title": "Presente",
        "description": (
            "Diseño, desarrollo, mantenimiento y actualización de arquitectura de sistemas completos."
            "Innovación e inclusión de IA en proyectos. "
            "Explorando, descubriendo y creando."
        ),
        "is_active": True,
    },
]

# --- Puntos clave del perfil ---

_KEY_POINTS: list[str] = [
    "Full-Stack con enfoque en backend e infraestructura",
    "Experiencia en entornos y despliegues cloud y on-premise",
    "Automatización como filosofía de trabajo",
]


def _bullet_point(text: str) -> rx.Component:
    """Renderiza un punto clave con bullet estilo terminal.

    Args:
        text: Texto del punto clave.

    Returns:
        Componente de texto con prefijo de viñeta.
    """
    return rx.hstack(
        rx.text(
            "▸",
            color=Color.ACCENT_CYAN,
            font_family=FontFamily.MONO,
            font_size=FontSize.BODY,
        ),
        rx.text(
            text,
            font_family=FontFamily.BODY,
            font_size=FontSize.BODY,
            color=Color.TEXT_PRIMARY,
            line_height="1.6",
        ),
        spacing="2",
        align_items="flex-start",
    )


def _bio_column() -> rx.Component:
    """Columna izquierda: UVP, tagline y puntos clave del perfil.

    Returns:
        Componente con la bio profesional completa.
    """
    return rx.vstack(
        # Propuesta de valor principal
        rx.text(
            UVP,
            font_family=FontFamily.BODY,
            font_size=FontSize.BODY,
            color=Color.TEXT_PRIMARY,
            line_height="1.8",
        ),
        # Tagline secundario
        rx.text(
            TAGLINE_BIO,
            font_size=FontSize.SMALL,
            color=Color.TEXT_SECONDARY,
            font_style="italic",
        ),
        # Puntos clave
        rx.vstack(
            *[_bullet_point(point) for point in _KEY_POINTS],
            spacing="3",
            width="100%",
        ),
        spacing="5",
        align_items="flex-start",
        width="100%",
    )


def _timeline_column() -> rx.Component:
    """Columna derecha: línea temporal profesional.

    Returns:
        Componente timeline con los hitos de carrera.
    """
    return rx.box(
        timeline(_TIMELINE_ITEMS),
        width="100%",
    )


def about_me_section() -> rx.Component:
    """Sección completa 'Sobre Mí' del portfolio.

    Layout responsivo: 2 columnas en escritorio (bio + timeline),
    1 columna en móvil. Incluye heading, bio profesional y
    línea temporal de carrera.

    Returns:
        Sección Sobre Mí lista para componer en la página principal.
    """
    return rx.box(
        rx.vstack(
            # Encabezado de sección
            rx.heading(
                "Sobre Mí",
                **HEADING_STYLE,
                font_size=["1.75rem", "2rem", "2.25rem"],
                as_="h1",
                width="100%",
                text_align="center",
            ),
            # Grid responsivo: 1 col móvil, 2 col desktop
            rx.grid(
                _bio_column(),
                _timeline_column(),
                grid_template_columns=["1fr", "1fr", "1fr 1fr"],
                gap=["2rem", "2rem", "3rem"],
                width="100%",
            ),
            spacing="7",
            align_items="flex-start",
            max_width=CONTAINER_MAX_WIDTH,
            width="100%",
            margin_x="auto",
        ),
        id="sobre-mi",
        as_="section",
        width="100%",
        **SECTION_PADDING,
        **SECTION_REVEAL,
    )
