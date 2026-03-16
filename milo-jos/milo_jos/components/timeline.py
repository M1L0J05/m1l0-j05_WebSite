"""Timeline — Línea temporal vertical para sección Sobre Mí.

Línea vertical con dots (estándar y activo con glow pulsante).
Fechas en monospace, descripciones en Inter.

Especificaciones: docs/architecture.md > Componentes UI > Timeline
"""

import reflex as rx

from milo_jos.styles import (
    Animation,
    Color,
    FontFamily,
    FontSize,
    FontWeight,
    GlassBg,
)


def timeline_item(
    *,
    year: str,
    title: str,
    description: str,
    is_active: bool = False,
) -> rx.Component:
    """Elemento individual del timeline.

    Args:
        year: Año o período (ej: '2023', '2024 - Presente').
        title: Título del hito.
        description: Descripción breve del hito.
        is_active: Si es el punto actual (glow pulsante).

    Returns:
        Componente de un item del timeline.
    """
    # Dot: activo (16px, cian, glow) vs estándar (12px, borde cian)
    dot_size = "16px" if is_active else "12px"
    dot_style: dict = {
        "width": dot_size,
        "height": dot_size,
        "min_width": dot_size,
        "border_radius": "50%",
        "flex_shrink": "0",
    }

    if is_active:
        dot_style.update({
            "background_color": Color.ACCENT_CYAN,
            "animation": Animation.GLOW_PULSE,
        })
    else:
        dot_style.update({
            "background_color": Color.BORDER,
            "border": f"2px solid {Color.ACCENT_CYAN}",
        })

    return rx.hstack(
        # Dot
        rx.box(**dot_style),
        # Contenido
        rx.vstack(
            rx.text(
                year,
                font_family=FontFamily.MONO,
                font_size=FontSize.SMALL,
                font_weight=FontWeight.REGULAR,
                color=Color.TEXT_SECONDARY,
            ),
            rx.text(
                title,
                font_family=FontFamily.HEADING,
                font_size=FontSize.H3,
                font_weight=FontWeight.SEMI_BOLD,
                color=Color.TEXT_PRIMARY,
            ),
            rx.text(
                description,
                font_family=FontFamily.BODY,
                font_size=FontSize.SMALL,
                color=Color.TEXT_SECONDARY,
                line_height="1.5",
            ),
            spacing="1",
            align_items="flex-start",
        ),
        spacing="4",
        align_items="flex-start",
        width="100%",
        position="relative",
    )


def timeline(items: list[dict]) -> rx.Component:
    """Timeline vertical completo.

    Args:
        items: Lista de dicts con keys: year, title, description, is_active.
            Ejemplo:
            [
                {"year": "2023", "title": "Inicio", "description": "...", "is_active": False},
                {"year": "2026", "title": "Presente", "description": "...", "is_active": True},
            ]

    Returns:
        Componente timeline vertical con línea conectora.
    """
    return rx.box(
        rx.vstack(
            *[
                timeline_item(
                    year=item["year"],
                    title=item["title"],
                    description=item["description"],
                    is_active=item.get("is_active", False),
                )
                for item in items
            ],
            spacing="6",
            width="100%",
            position="relative",
        ),
        # Línea vertical conectora (pseudo-element via CSS)
        position="relative",
        _before={
            "content": "''",
            "position": "absolute",
            "left": "7px",
            "top": "8px",
            "bottom": "8px",
            "width": "2px",
            "background_color": Color.BORDER,
        },
        padding_left="0",
    )
