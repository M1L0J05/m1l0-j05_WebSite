"""Badge — Etiqueta de tecnología tipo terminal.

Se usa para tags de stack técnico, estados de proyecto, versiones.
Estilo monospace, fondo cian traslúcido, borde sutil.

Especificaciones: docs/architecture.md > Componentes UI > Badge
"""

import reflex as rx

from milo_jos.styles import Color, FontFamily, FontSize, FontWeight, GlassBg


def badge(
    text: str,
    *,
    color: str = Color.ACCENT_CYAN,
    bg: str = GlassBg.ACCENT_CYAN_10,
    border_color: str = GlassBg.ACCENT_CYAN_30,
) -> rx.Component:
    """Etiqueta/badge para tecnologías, estados o versiones.

    Args:
        text: Texto a mostrar (se renderiza en uppercase).
        color: Color del texto.
        bg: Color de fondo.
        border_color: Color del borde.

    Returns:
        Componente badge estilizado.
    """
    return rx.text(
        text,
        font_family=FontFamily.MONO,
        font_size=FontSize.MICRO,
        font_weight=FontWeight.REGULAR,
        text_transform="uppercase",
        letter_spacing="0.05em",
        color=color,
        background=bg,
        border=f"1px solid {border_color}",
        border_radius="6px",
        padding_x="0.625rem",
        padding_y="0.25rem",
        white_space="nowrap",
        _hover={
            "border_color": GlassBg.ACCENT_CYAN_60,
            "transform": "scale(1.05)",
        },
        transition="border-color 0.2s ease, transform 0.2s ease",
        cursor="default",
    )


def status_badge(status: str) -> rx.Component:
    """Badge semántico para estados de proyecto.

    Args:
        status: Estado del proyecto ('PRODUCCIÓN', 'LAB', 'EN DESARROLLO').

    Returns:
        Badge con color apropiado según el estado.
    """
    # Mapeo estado → color
    color_map: dict[str, str] = {
        "PRODUCCIÓN": Color.ACCENT_GREEN,
        "PROD": Color.ACCENT_GREEN,
        "LAB": Color.ACCENT_ORANGE,
        "EN DESARROLLO": Color.ACCENT_CYAN,
        "DEV": Color.ACCENT_CYAN,
    }

    status_upper = status.upper()
    accent = color_map.get(status_upper, Color.TEXT_SECONDARY)

    return badge(
        status_upper,
        color=accent,
        bg=f"rgba({_hex_to_rgb(accent)}, 0.1)",
        border_color=f"rgba({_hex_to_rgb(accent)}, 0.3)",
    )


def _hex_to_rgb(hex_color: str) -> str:
    """Convierte un color hex (#RRGGBB) a string 'R, G, B'.

    Args:
        hex_color: Color en formato '#RRGGBB'.

    Returns:
        String con componentes RGB separados por coma.
    """
    hex_color = hex_color.lstrip("#")
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return f"{r}, {g}, {b}"
