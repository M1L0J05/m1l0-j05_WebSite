"""Paquete de estilos — milo-jos.es v2.0.

Re-exporta los tokens y utilidades de diseño para importación
conveniente desde el resto de la aplicación:

    from milo_jos.styles import Color, FontFamily, BASE_STYLE
"""

from .animations import Animation, get_all_keyframes
from .colors import Color, COLOR_TOKENS, GlassBg
from .fonts import FontFamily, FontSize, FontWeight
from .styles import (
    BASE_STYLE,
    Breakpoint,
    CONTAINER_MAX_WIDTH,
    GLASS_CARD,
    GLASS_CARD_HOVER,
    GLASS_NAVBAR,
    HEADING_STYLE,
    LABEL_STYLE,
    MONO_STYLE,
    SECTION_PADDING,
    SECTION_REVEAL,
    SUBHEADING_STYLE,
)

__all__: list[str] = [
    # colors
    "Color",
    "COLOR_TOKENS",
    "GlassBg",
    # fonts
    "FontFamily",
    "FontSize",
    "FontWeight",
    # styles
    "BASE_STYLE",
    "Breakpoint",
    "CONTAINER_MAX_WIDTH",
    "GLASS_CARD",
    "GLASS_CARD_HOVER",
    "GLASS_NAVBAR",
    "HEADING_STYLE",
    "LABEL_STYLE",
    "MONO_STYLE",
    "SECTION_PADDING",
    "SECTION_REVEAL",
    "SUBHEADING_STYLE",
    # animations
    "Animation",
    "get_all_keyframes",
]
