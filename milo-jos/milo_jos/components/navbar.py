"""Navbar — Barra de navegación principal de milo-jos.es.

Sticky top con glassmorphism al scroll. Wordmark a la izquierda,
enlaces de ancla a las secciones, CTA "Contactar" a la derecha.
En mobile: wordmark + CTA únicamente (sin drawer).

Especificaciones: docs/architecture.md > Componentes UI > Navbar
"""

import reflex as rx

from milo_jos.styles import (
    Color,
    FontFamily,
    FontSize,
    FontWeight,
    GLASS_NAVBAR,
    GlassBg,
)
from milo_jos.utils import NAV_ITEMS, WORDMARK_NAVBAR


# =============================================================================
# Sub-componentes
# =============================================================================

def _wordmark() -> rx.Component:
    """Wordmark 'M1L0_J05' con fuente monospace y color cian."""
    return rx.link(
        rx.text(
            WORDMARK_NAVBAR,
            font_family=FontFamily.MONO,
            font_weight=FontWeight.EXTRA_BOLD,
            font_size=FontSize.H2,
            color=Color.ACCENT_CYAN,
            _hover={"opacity": "0.8"},
            transition="opacity 0.2s ease",
        ),
        href="/",
        underline="none",
    )


def _nav_link(label: str, href: str) -> rx.Component:
    """Enlace de navegación individual (desktop)."""
    return rx.link(
        rx.text(
            label,
            font_family=FontFamily.BODY,
            font_size=FontSize.BODY,
            font_weight=FontWeight.MEDIUM,
            color=Color.TEXT_SECONDARY,
            _hover={"color": Color.ACCENT_CYAN},
            transition="color 0.2s ease",
        ),
        href=f"/{href}",
        underline="none",
    )


def _nav_links_desktop() -> rx.Component:
    """Grupo de enlaces de navegación para desktop."""
    return rx.hstack(
        *[_nav_link(item["label"], item["href"]) for item in NAV_ITEMS],
        spacing="6",
        align_items="center",
    )


def _cta_button() -> rx.Component:
    """Botón CTA 'Contactar' (outline cian)."""
    return rx.link(
        rx.text(
            "Contactar",
            font_family=FontFamily.HEADING,
            font_size=FontSize.SMALL,
            font_weight=FontWeight.SEMI_BOLD,
            color=Color.ACCENT_CYAN,
            padding_x="1rem",
            padding_y="0.5rem",
            border=f"1px solid {Color.ACCENT_CYAN}",
            border_radius="8px",
            _hover={
                "background": GlassBg.ACCENT_CYAN_10,
            },
            transition="background 0.2s ease",
        ),
        href="/#contacto",
        underline="none",
    )


# =============================================================================
# Componente principal
# =============================================================================

def navbar() -> rx.Component:
    """Barra de navegación principal.

    - Desktop: wordmark + links de ancla + CTA en una línea
    - Mobile/Tablet: wordmark + CTA (sin drawer)

    Returns:
        Componente Reflex con la navbar completa.
    """
    return rx.box(
        # Desktop
        rx.desktop_only(
            rx.hstack(
                _wordmark(),
                rx.spacer(),
                _nav_links_desktop(),
                _cta_button(),
                align_items="center",
                width="100%",
                margin_x="auto",
                padding_x="2rem",
            ),
            width="100%",
        ),
        # Mobile y tablet: solo wordmark + CTA
        rx.mobile_and_tablet(
            rx.hstack(
                _wordmark(),
                rx.spacer(),
                _cta_button(),
                align_items="center",
                width="100%",
                padding_x="1.5rem",
            ),
            width="100%",
        ),
        # Estilos del contenedor
        position="sticky",
        top="0",
        z_index="40",
        width="100%",
        height=["56px", "56px", "64px"],
        display="flex",
        align_items="center",
        **GLASS_NAVBAR,
    )
