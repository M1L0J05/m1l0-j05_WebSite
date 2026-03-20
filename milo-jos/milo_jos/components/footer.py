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

            # Copyright + easter egg + versión
            rx.hstack(
                rx.text(
                    f"\u00a9 {year_range} ",
                    font_family=FontFamily.MONO,
                    font_size=FontSize.MICRO,
                    color=Color.TEXT_SECONDARY,
                ),
                rx.text(
                    rx.text.span("I "),
                    rx.text.span(
                        "LoVe",
                        color="red",
                        font_weight=FontWeight.BOLD,
                    ),
                    rx.text.span(" Linares!"),
                    font_family=FontFamily.MONO,
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
            padding_x=["1.5rem", "2rem"],
            padding_y=["2rem", "3rem"],
        ),
        width="100%",
        border_top=f"1px solid {Color.BORDER}",
        background_color=Color.BG_BASE,
    )
