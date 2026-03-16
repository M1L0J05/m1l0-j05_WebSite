"""Button — Botones primario (CTA) y secundario (outline).

Dos variantes con estilos coherentes al sistema de diseño.
Tipografía Outfit 600, border-radius 8px, transiciones suaves.

Especificaciones: docs/architecture.md > Componentes UI > Button
"""

import reflex as rx

from milo_jos.styles import Color, FontFamily, FontSize, FontWeight, GlassBg


def primary_button(
    text: str,
    *,
    href: str = "#",
    on_click: rx.EventHandler | None = None,
) -> rx.Component:
    """Botón primario CTA (fondo cian, texto oscuro).

    Args:
        text: Texto del botón.
        href: URL de destino (si es enlace).
        on_click: Handler de evento (si es acción).

    Returns:
        Componente botón primario.
    """
    btn = rx.text(
        text,
        font_family=FontFamily.HEADING,
        font_size=FontSize.SMALL,
        font_weight=FontWeight.SEMI_BOLD,
        color=Color.BG_BASE,
        background_color=Color.ACCENT_CYAN,
        padding_x="1.75rem",
        padding_y="0.75rem",
        border_radius="8px",
        cursor="pointer",
        _hover={
            "filter": "brightness(1.15)",
            "box_shadow": f"0 0 16px {GlassBg.GLOW_CYAN}",
        },
        transition="filter 0.2s ease, box-shadow 0.2s ease",
        text_align="center",
        display="inline-block",
    )

    if on_click is not None:
        return rx.box(btn, on_click=on_click, cursor="pointer")

    return rx.link(btn, href=href, underline="none")


def secondary_button(
    text: str,
    *,
    href: str = "#",
    on_click: rx.EventHandler | None = None,
) -> rx.Component:
    """Botón secundario (outline cian, fondo transparente).

    Args:
        text: Texto del botón.
        href: URL de destino (si es enlace).
        on_click: Handler de evento (si es acción).

    Returns:
        Componente botón secundario.
    """
    btn = rx.text(
        text,
        font_family=FontFamily.HEADING,
        font_size=FontSize.SMALL,
        font_weight=FontWeight.SEMI_BOLD,
        color=Color.ACCENT_CYAN,
        background="transparent",
        border=f"1px solid {Color.ACCENT_CYAN}",
        padding_x="1.75rem",
        padding_y="0.75rem",
        border_radius="8px",
        cursor="pointer",
        _hover={
            "background": GlassBg.ACCENT_CYAN_10,
        },
        transition="background 0.2s ease",
        text_align="center",
        display="inline-block",
    )

    if on_click is not None:
        return rx.box(btn, on_click=on_click, cursor="pointer")

    return rx.link(btn, href=href, underline="none")
