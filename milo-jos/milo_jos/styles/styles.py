"""Estilos base — BASE_STYLE, glassmorphism y breakpoints.

Define el diccionario de estilos globales que se pasa a rx.App(style=...)
y helpers reutilizables para glassmorphism y responsive.
"""

from .colors import Color, GlassBg
from .fonts import FontFamily, FontSize, FontWeight


# =============================================================================
# Breakpoints (min-width)
# =============================================================================

class Breakpoint:
    """Breakpoints del sistema responsive (mobile-first).

    | Nombre     | Rango             | Columnas grid |
    |------------|-------------------|---------------|
    | MOBILE     | 320px – 767px     | 1             |
    | TABLET     | 768px – 1023px    | 2             |
    | DESKTOP    | 1024px – 1439px   | 3-4           |
    | DESKTOP_XL | 1440px+           | 4             |
    """

    MOBILE: str = "320px"
    TABLET: str = "768px"
    DESKTOP: str = "1024px"
    DESKTOP_XL: str = "1440px"


# =============================================================================
# Estilos globales (rx.App style dict)
# =============================================================================

BASE_STYLE: dict = {
    "font_family": FontFamily.BODY,
    "font_size": FontSize.BODY,
    "font_weight": FontWeight.REGULAR,
    "color": Color.TEXT_PRIMARY,
    "background_color": Color.BG_BASE,
    "line_height": "1.6",
    # Reset suave
    "margin": "0",
    "padding": "0",
    "box_sizing": "border-box",
    # Scroll suave para anclas SPA
    "scroll_behavior": "smooth",
    # Selección de texto
    "::selection": {
        "background_color": GlassBg.ACCENT_CYAN_30,
        "color": Color.TEXT_PRIMARY,
    },
}


# =============================================================================
# Glassmorphism helpers (dicts listos para spread en props)
# =============================================================================

GLASS_CARD: dict = {
    "background": GlassBg.CARD,
    "backdrop_filter": "blur(12px)",
    "border": f"1px solid {GlassBg.BORDER}",
    "border_radius": "12px",
}
"""Card base con glassmorphism."""

GLASS_CARD_HOVER: dict = {
    "box_shadow": f"0 0 20px {GlassBg.GLOW_CYAN}",
    "transform": "translateY(-4px)",
    "transition": "box-shadow 0.3s ease, transform 0.3s ease",
}
"""Hover state para cards (glow + lift)."""

GLASS_NAVBAR: dict = {
    "background": GlassBg.CARD,
    "backdrop_filter": "blur(16px)",
    "border_bottom": f"1px solid {GlassBg.BORDER}",
}
"""Navbar con glassmorphism más intenso."""


# =============================================================================
# Mixins de estilo reutilizables
# =============================================================================

HEADING_STYLE: dict = {
    "font_family": FontFamily.HEADING,
    "font_weight": FontWeight.BOLD,
    "color": Color.TEXT_PRIMARY,
    "line_height": "1.2",
}
"""Estilo base para títulos (H1-H2)."""

SUBHEADING_STYLE: dict = {
    "font_family": FontFamily.HEADING,
    "font_weight": FontWeight.MEDIUM,
    "color": Color.TEXT_PRIMARY,
    "line_height": "1.3",
}
"""Estilo base para subtítulos (H3-H4)."""

MONO_STYLE: dict = {
    "font_family": FontFamily.MONO,
    "font_weight": FontWeight.REGULAR,
}
"""Estilo base para texto monospace (tags, código, labels)."""

LABEL_STYLE: dict = {
    "font_family": FontFamily.MONO,
    "font_size": FontSize.MICRO,
    "font_weight": FontWeight.REGULAR,
    "text_transform": "uppercase",
    "letter_spacing": "0.05em",
    "color": Color.TEXT_SECONDARY,
}
"""Estilo para labels y metadatos pequeños."""

SECTION_PADDING: dict = {
    "padding_x": ["1.5rem", "2rem", "4rem", "6rem"],
    "padding_y": "5rem",
}
"""Padding responsive para secciones principales."""

CONTAINER_MAX_WIDTH: str = "1200px"
"""Ancho máximo del contenedor principal."""
