"""Card — Tarjeta de proyecto con glassmorphism.

Efecto glass base + hover con glow cian y translateY(-4px).
Contiene: badge de estado, nombre, descripción, stack badges y botones.

Especificaciones: docs/architecture.md > Componentes UI > Card
"""

from typing import Any

import reflex as rx

from milo_jos.styles import (
    Color,
    FontFamily,
    FontSize,
    FontWeight,
    GLASS_CARD,
    GlassBg,
    HEADING_STYLE,
)
from milo_jos.components.badge import badge, status_badge


def project_card(
    *,
    name: str,
    description: str,
    status: str,
    tech_stack: list[str],
    href: str = "#",
    image_src: str | None = None,
) -> rx.Component:
    """Tarjeta de proyecto con glassmorphism.

    Args:
        name: Nombre del proyecto.
        description: Descripción breve.
        status: Estado ('PRODUCCIÓN', 'LAB', 'EN DESARROLLO').
        tech_stack: Lista de tecnologías.
        href: URL de detalle del proyecto.
        image_src: Ruta a la imagen/screenshot (opcional).

    Returns:
        Componente card estilizado.
    """
    children: list[Any] = []

    # Imagen (si existe)
    if image_src:
        children.append(
            rx.box(
                rx.image(
                    src=image_src,
                    width="100%",
                    height="180px",
                    object_fit="cover",
                    border_radius="8px 8px 0 0",
                    alt=f"Screenshot de {name}",
                ),
                width="100%",
                overflow="hidden",
            )
        )

    # Contenido
    children.extend([
        # Badge de estado
        status_badge(status),
        # Nombre del proyecto
        rx.text(
            name,
            **HEADING_STYLE,
            font_size=FontSize.H3,
            margin_top="0.5rem",
        ),
        # Descripción
        rx.text(
            description,
            font_family=FontFamily.BODY,
            font_size=FontSize.SMALL,
            color=Color.TEXT_SECONDARY,
            line_height="1.5",
            margin_top="0.5rem",
        ),
        # Stack badges
        rx.hstack(
            *[badge(tech) for tech in tech_stack],
            flex_wrap="wrap",
            spacing="2",
            margin_top="1rem",
        ),
    ])

    return rx.link(
        rx.box(
            rx.vstack(
                *children,
                align_items="flex-start",
                spacing="1",
                padding="1.5rem",
                width="100%",
            ),
            width="100%",
            **GLASS_CARD,
            _hover={
                "box_shadow": f"0 0 20px {GlassBg.GLOW_CYAN}",
                "transform": "translateY(-4px)",
            },
            transition="box-shadow 0.3s ease, transform 0.3s ease",
            overflow="hidden",
        ),
        href=href,
        underline="none",
        width="100%",
    )


def coming_soon_card() -> rx.Component:
    """Tarjeta placeholder 'Coming Soon'.

    Returns:
        Card con estilo atenuado indicando proyecto futuro.
    """
    return rx.box(
        rx.vstack(
            rx.icon(
                "plus",
                size=32,
                color=Color.TEXT_SECONDARY,
            ),
            rx.text(
                "Coming Soon",
                font_family=FontFamily.MONO,
                font_size=FontSize.SMALL,
                color=Color.TEXT_SECONDARY,
            ),
            align="center",
            justify="center",
            spacing="3",
            padding="2rem",
            width="100%",
            min_height="200px",
        ),
        width="100%",
        **GLASS_CARD,
        opacity="0.5",
        border_style="dashed",
    )
