"""Tokens de color — Paleta dark-first para milo-jos.es.

Filosofía: optimizada para glassmorphism, contraste WCAG AA
y coherencia con interfaces CLI.

Cada token se expone como constante de módulo para uso directo
en props de Reflex (bg=Color.BG_BASE) y como diccionario
COLOR_TOKENS para iteración programática.
"""


class Color:
    """Paleta de 10 tokens semánticos de color."""

    # --- Fondos ---
    BG_BASE: str = "#0D1117"
    """Fondo raíz de la aplicación."""

    BG_CARD: str = "#161B22"
    """Fondo de cards y paneles."""

    BG_ELEVATED: str = "#1C2128"
    """Fondo de tooltips, modales y elementos elevados."""

    # --- Acentos ---
    ACCENT_CYAN: str = "#00B4D8"
    """CTA, links, glow, wordmark."""

    ACCENT_ORANGE: str = "#FF6B2B"
    """Hover states, badges activos."""

    ACCENT_GREEN: str = "#3FB950"
    """Estado online, deploys activos."""

    # --- Texto ---
    TEXT_PRIMARY: str = "#E6EDF3"
    """Texto principal (body, títulos)."""

    TEXT_SECONDARY: str = "#8B949E"
    """Metadatos, fechas, labels, prompt prefix."""

    # --- Utilidad ---
    BORDER: str = "#30363D"
    """Divisores, bordes de card."""

    ERROR: str = "#F85149"
    """Alertas, errores."""


class GlassBg:
    """Valores RGBA para efecto glassmorphism."""

    CARD: str = "rgba(22, 27, 34, 0.6)"
    """Fondo semitransparente de card."""

    CARD_FALLBACK: str = "rgba(22, 27, 34, 0.95)"
    """Fallback para navegadores sin backdrop-filter."""

    BORDER: str = "rgba(48, 54, 61, 0.8)"
    """Borde semitransparente para glass."""

    GLOW_CYAN: str = "rgba(0, 180, 216, 0.15)"
    """Sombra glow cian en hover."""

    ACCENT_CYAN_10: str = "rgba(0, 180, 216, 0.1)"
    """Fondo de badges (cian al 10%)."""

    ACCENT_CYAN_30: str = "rgba(0, 180, 216, 0.3)"
    """Borde de badges (cian al 30%)."""

    ACCENT_CYAN_60: str = "rgba(0, 180, 216, 0.6)"
    """Borde de badges en hover (cian al 60%)."""


# Diccionario completo para iteración (ej: generar CSS variables)
COLOR_TOKENS: dict[str, str] = {
    "bg-base": Color.BG_BASE,
    "bg-card": Color.BG_CARD,
    "bg-elevated": Color.BG_ELEVATED,
    "accent-cyan": Color.ACCENT_CYAN,
    "accent-orange": Color.ACCENT_ORANGE,
    "accent-green": Color.ACCENT_GREEN,
    "text-primary": Color.TEXT_PRIMARY,
    "text-secondary": Color.TEXT_SECONDARY,
    "border": Color.BORDER,
    "error": Color.ERROR,
}
