"""Footer — Pie de página de milo-jos.es.

Minimalista: links sociales, copyright dinámico y versión
importada desde version.py.

Especificaciones: docs/architecture.md > Componentes UI > Footer
"""

from datetime import datetime

import reflex as rx

from milo_jos.styles import Color, FontFamily, FontSize, FontWeight
from milo_jos.utils import (
    COPYRIGHT_YEAR_START,
    FOOTER_VERSION,
    SOCIAL_LINKS,
    WORDMARK_FOOTER,
)


def _social_link(name: str, url: str, icon: str) -> rx.Component:
    """Enlace social individual con icono Lucide."""
    return rx.link(
        rx.hstack(
            rx.icon(icon, size=16, color=Color.TEXT_SECONDARY),
            rx.text(
                name,
                font_family=FontFamily.BODY,
                font_size=FontSize.SMALL,
                color=Color.TEXT_SECONDARY,
                _hover={"color": Color.ACCENT_CYAN},
                transition="color 0.2s ease",
            ),
            spacing="2",
            align_items="center",
        ),
        href=url,
        is_external=True,
        underline="none",
    )


def footer() -> rx.Component:
    """Pie de página con links sociales, copyright y versión.

    Returns:
        Componente Reflex con el footer completo.
    """
    current_year = datetime.now().year
    year_range = (
        f"{COPYRIGHT_YEAR_START}-{current_year}"
        if current_year > COPYRIGHT_YEAR_START
        else str(COPYRIGHT_YEAR_START)
    )

    return rx.box(
        rx.vstack(
            # Links sociales
            rx.hstack(
                *[
                    _social_link(link["name"], link["url"], link["icon"])
                    for link in SOCIAL_LINKS
                ],
                spacing="6",
                justify="center",
                flex_wrap="wrap",
            ),
            # Separador
            rx.divider(
                border_color=Color.BORDER,
                width="100%",
                max_width="200px",
            ),
            # Copyright + versión
            rx.hstack(
                rx.text(
                    f"\u00a9 {year_range} ",
                    rx.text.span(
                        WORDMARK_FOOTER,
                        font_family=FontFamily.MONO,
                        font_weight=FontWeight.REGULAR,
                        color=Color.ACCENT_CYAN,
                    ),
                    font_family=FontFamily.BODY,
                    font_size=FontSize.MICRO,
                    color=Color.TEXT_SECONDARY,
                ),
                rx.text(
                    FOOTER_VERSION,
                    font_family=FontFamily.MONO,
                    font_size=FontSize.MICRO,
                    color=Color.TEXT_SECONDARY,
                ),
                spacing="4",
                align_items="center",
            ),
            spacing="4",
            align="center",
            width="100%",
            max_width="1200px",
            margin_x="auto",
            padding_x="2rem",
            padding_y="3rem",
        ),
        width="100%",
        border_top=f"1px solid {Color.BORDER}",
        background_color=Color.BG_BASE,
    )
