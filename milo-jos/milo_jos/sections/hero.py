"""Sección Hero — Viewport completo con wordmark, terminal y CTAs.

Primer impacto visual del portfolio: gradiente animado de fondo,
wordmark >_ M1L0_J05 con cursor parpadeante, tagline, bloque de
terminal simulado y botones de acción principal.

Especificaciones: docs/architecture.md > Secciones > Hero
"""

import reflex as rx

from milo_jos.styles import (
    Animation,
    Color,
    FontFamily,
    FontSize,
    FontWeight,
    SECTION_PADDING,
    CONTAINER_MAX_WIDTH,
)
from milo_jos.utils.constants import TAGLINE_HERO, WORDMARK_HERO
from milo_jos.components import (
    terminal_block,
    primary_button,
    secondary_button,
)


# ─── Constantes internas de la sección ───────────────────────────────────────

# Gradiente animado del fondo hero
_HERO_BG_GRADIENT: str = (
    f"linear-gradient(135deg, {Color.BG_BASE} 0%, #0a1628 25%, "
    f"{Color.BG_BASE} 50%, #0d1f2d 75%, {Color.BG_BASE} 100%)"
)

# Líneas del bloque de terminal
_TERMINAL_LINES: list[dict] = [
    {"command": "whoami"},
    {"output": "m1l0_j05 — Full-Stack Engineer & DevOps"},
    {"command": "cat mission.txt"},
    {"output": "Building systems. Automating the rest."},
]


# ─── Componentes internos ────────────────────────────────────────────────────


def _wordmark() -> rx.Component:
    """Wordmark principal con prefijo >_ y cursor █ parpadeante.

    El prefijo se muestra en TEXT_SECONDARY y el nombre en ACCENT_CYAN.
    El cursor utiliza la animación CURSOR_BLINK (step-end infinite).

    Returns:
        Componente de texto con el wordmark estilizado.
    """
    # Separar prefijo ">_ " del nombre "M1L0_J05"
    prefix = ">_ "
    name = WORDMARK_HERO.replace(">_", "")

    return rx.heading(
        rx.text.span(
            prefix,
            color=Color.TEXT_SECONDARY,
        ),
        rx.text.span(
            name,
            color=Color.ACCENT_CYAN,
        ),
        rx.text.span(
            "|",
            color=Color.ACCENT_CYAN,
            animation=Animation.CURSOR_BLINK,
        ),
        font_family=FontFamily.MONO,
        font_weight=FontWeight.EXTRA_BOLD,
        font_size=["2.5rem", "2.5rem", "3.5rem", "4.5rem"],
        line_height="1.2",
        as_="h1",
    )


def _tagline() -> rx.Component:
    """Tagline principal debajo del wordmark.

    Utiliza la fuente Outfit con tamaño H2 y color TEXT_PRIMARY.

    Returns:
        Componente de texto con el tagline del hero.
    """
    return rx.text(
        TAGLINE_HERO,
        font_family=FontFamily.HEADING,
        font_size=["1.25rem", "1.5rem", "2rem", "2.25rem"],
        font_weight=FontWeight.MEDIUM,
        color=Color.TEXT_PRIMARY,
        line_height="1.4",
        text_align="center",
    )


def _cta_buttons() -> rx.Component:
    """Fila de botones CTA: Ver Proyectos (primario) y Contactar (secundario).

    Returns:
        HStack con los dos botones de acción.
    """
    return rx.hstack(
        primary_button("Ver Proyectos", href="#proyectos"),
        secondary_button("Contactar", href="#contacto"),
        spacing="4",
        justify="center",
        wrap="wrap",
    )


def _scroll_indicator() -> rx.Component:
    """Indicador de scroll con flecha hacia abajo y animación bounce.

    Se posiciona en la parte inferior de la sección hero para
    invitar al usuario a hacer scroll.

    Returns:
        Componente con icono de flecha animada.
    """
    return rx.link(
        rx.box(
            rx.icon(
                "chevron-down",
                size=36,
                color=Color.TEXT_SECONDARY,
            ),
            animation=Animation.SCROLL_BOUNCE,
            padding_top="3rem",
            opacity="0.7",
            _hover={"opacity": "1"},
            transition="opacity 0.2s ease",
            cursor="pointer",
        ),
        href="#stack",
        underline="none",
    )


# ─── Sección exportada ──────────────────────────────────────────────────────


def hero_section() -> rx.Component:
    """Sección hero a viewport completo con gradiente animado.

    Estructura vertical centrada:
    1. Wordmark >_ M1L0_J05 con cursor parpadeante
    2. Tagline principal
    3. Bloque de terminal simulado
    4. Botones CTA (Ver Proyectos / Contactar)
    5. Indicador de scroll (flecha bounce)

    Returns:
        Componente de sección hero completo con id='hero'.
    """
    return rx.box(
        rx.vstack(
            _wordmark(),
            _tagline(),
            terminal_block(
                _TERMINAL_LINES,
                title="terminal",
            ),
            _cta_buttons(),
            _scroll_indicator(),
            spacing="8",
            align="center",
            justify="center",
            max_width=CONTAINER_MAX_WIDTH,
            width="100%",
            **SECTION_PADDING,
        ),
        id="hero",
        display="flex",
        align_items="center",
        justify_content="center",
        min_height="100vh",
        width="100%",
        # Patrón circuit-board en mosaico (encima) + gradiente estático (debajo)
        background_image=f"url('/images/root/circuit-board.svg'), {_HERO_BG_GRADIENT}",
        background_size="250px 250px, 100% 100%",
        background_repeat="repeat, no-repeat",
    )
