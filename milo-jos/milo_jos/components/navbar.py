"""Navbar — Barra de navegación principal de milo-jos.es.

Sticky top con glassmorphism al scroll. Wordmark a la izquierda,
enlaces de ancla a las secciones, CTA "Contactar" a la derecha.
En mobile: drawer lateral con fondo oscuro.

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
# Estado del drawer mobile
# =============================================================================

class NavbarState(rx.State):
    """Estado para controlar la apertura/cierre del drawer mobile."""

    is_drawer_open: bool = False

    @rx.event
    def toggle_drawer(self) -> None:
        """Alterna el estado del drawer."""
        self.is_drawer_open = not self.is_drawer_open

    @rx.event
    def close_drawer(self) -> None:
        """Cierra el drawer (usado al hacer click en un enlace)."""
        self.is_drawer_open = False


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
            font_size=FontSize.H3,
            color=Color.ACCENT_CYAN,
            _hover={"opacity": "0.8"},
            transition="opacity 0.2s ease",
        ),
        href="#hero",
        underline="none",
    )


def _nav_link(label: str, href: str) -> rx.Component:
    """Enlace de navegación individual (desktop)."""
    return rx.link(
        rx.text(
            label,
            font_family=FontFamily.BODY,
            font_size=FontSize.SMALL,
            font_weight=FontWeight.MEDIUM,
            color=Color.TEXT_SECONDARY,
            _hover={"color": Color.ACCENT_CYAN},
            transition="color 0.2s ease",
        ),
        href=href,
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
            padding_x="1.25rem",
            padding_y="0.5rem",
            border=f"1px solid {Color.ACCENT_CYAN}",
            border_radius="8px",
            _hover={
                "background": GlassBg.ACCENT_CYAN_10,
            },
            transition="background 0.2s ease",
        ),
        href="#contacto",
        underline="none",
    )


def _drawer_nav_link(label: str, href: str) -> rx.Component:
    """Enlace de navegación para el drawer mobile."""
    return rx.link(
        rx.text(
            label,
            font_family=FontFamily.BODY,
            font_size=FontSize.H3,
            font_weight=FontWeight.MEDIUM,
            color=Color.TEXT_SECONDARY,
            _hover={"color": Color.ACCENT_CYAN},
            padding_y="0.75rem",
            transition="color 0.2s ease",
        ),
        href=href,
        underline="none",
        on_click=NavbarState.close_drawer,
        width="100%",
    )


def _mobile_drawer() -> rx.Component:
    """Drawer lateral para navegación mobile."""
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon(
                "menu",
                size=28,
                color=Color.TEXT_PRIMARY,
                cursor="pointer",
            ),
            on_click=NavbarState.toggle_drawer,
        ),
        rx.drawer.overlay(z_index="50"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    # Cabecera del drawer
                    rx.hstack(
                        _wordmark(),
                        rx.spacer(),
                        rx.drawer.close(
                            rx.icon(
                                "x",
                                size=28,
                                color=Color.TEXT_SECONDARY,
                                cursor="pointer",
                            ),
                            on_click=NavbarState.close_drawer,
                        ),
                        width="100%",
                        align_items="center",
                    ),
                    # Separador
                    rx.divider(border_color=Color.BORDER),
                    # Enlaces
                    *[
                        _drawer_nav_link(item["label"], item["href"])
                        for item in NAV_ITEMS
                    ],
                    # Separador
                    rx.spacer(),
                    rx.divider(border_color=Color.BORDER),
                    # CTA
                    rx.link(
                        rx.text(
                            "Contactar",
                            font_family=FontFamily.HEADING,
                            font_size=FontSize.H3,
                            font_weight=FontWeight.SEMI_BOLD,
                            color=Color.ACCENT_CYAN,
                        ),
                        href="#contacto",
                        underline="none",
                        on_click=NavbarState.close_drawer,
                    ),
                    spacing="3",
                    width="100%",
                    padding="1.5rem",
                    height="100%",
                ),
                height="100%",
                width="80vw",
                max_width="320px",
                background_color=Color.BG_BASE,
                border_right=f"1px solid {Color.BORDER}",
            ),
        ),
        open=NavbarState.is_drawer_open,
        direction="left",
        modal=True,
    )


# =============================================================================
# Componente principal
# =============================================================================

def navbar() -> rx.Component:
    """Barra de navegación principal.

    - Desktop: wordmark + links + CTA en una línea
    - Mobile/Tablet: wordmark + hamburger → drawer lateral

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
                max_width="1200px",
                margin_x="auto",
                padding_x="2rem",
            ),
        ),
        # Mobile y tablet
        rx.mobile_and_tablet(
            rx.hstack(
                _wordmark(),
                rx.spacer(),
                _mobile_drawer(),
                align_items="center",
                width="100%",
                padding_x="1.5rem",
            ),
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
