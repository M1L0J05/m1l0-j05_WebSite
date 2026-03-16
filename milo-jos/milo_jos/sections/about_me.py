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
    CONTAINER_MAX_WIDTH,
)
from milo_jos.utils.constants import TAGLINE_BIO, UVP
from milo_jos.components import timeline, timeline_item


# --- Datos del timeline profesional ---

_TIMELINE_ITEMS: list[dict] = [
    {
        "year": "2023",
        "title": "Inicio en desarrollo web",
        "description": (
            "Primeros proyectos con Python y JavaScript. "
            "Fundamentos de programación y diseño web."
        ),
        "is_active": False,
    },
    {
        "year": "2024",
        "title": "Full-Stack & DevOps",
        "description": (
            "Transición a infraestructura. Docker, Kubernetes, CI/CD. "
            "Proyectos propios en producción."
        ),
        "is_active": False,
    },
    {
        "year": "2025",
        "title": "Infraestructura & Automatización",
        "description": (
            "Homelab con Proxmox. Terraform, Ansible. "
            "Pipelines de automatización."
        ),
        "is_active": False,
    },
    {
        "year": "2026",
        "title": "Presente",
        "description": (
            "Arquitectura de sistemas completos. Consultoría freelance. "
            "Construcción de milo-jos.es v2.0."
        ),
        "is_active": True,
    },
]

# --- Puntos clave del perfil ---

_KEY_POINTS: list[str] = [
    "Ingeniero Full-Stack con enfoque en backend e infraestructura",
    "Basado en Sevilla, España",
    "Experiencia en entornos cloud y on-premise",
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
                size="8",
                as_="h1",
            ),
            # Grid responsivo: 1 col móvil, 2 col desktop
            rx.grid(
                _bio_column(),
                _timeline_column(),
                grid_template_columns=["1fr", "1fr", "1fr 1fr"],
                gap="3rem",
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
    )
