"""Sistema tipográfico — JetBrains Mono, Outfit, Inter.

Tres familias con roles definidos, self-hosted en woff2.
Las fuentes se sirven desde assets/fonts/ vía fonts.css.

Módulo de referencia: docs/identity-system.md
"""


class FontFamily:
    """Familias tipográficas y su rol en el sistema de diseño."""

    MONO: str = "JetBrains Mono, monospace"
    """Display (wordmark), bloques de código, tags, badges, versiones."""

    HEADING: str = "Outfit, sans-serif"
    """Títulos de sección (H1-H4), subtítulos, nombres de proyecto."""

    BODY: str = "Inter, sans-serif"
    """Texto corrido, párrafos, descripciones."""


class FontWeight:
    """Pesos tipográficos usados en el sistema."""

    REGULAR: str = "400"
    MEDIUM: str = "500"
    SEMI_BOLD: str = "600"
    BOLD: str = "700"
    EXTRA_BOLD: str = "800"


class FontSize:
    """Escala tipográfica en rem (base 16px).

    | Nivel   | rem    | px equiv |
    |---------|--------|----------|
    | DISPLAY | 3.5rem | 56px     |
    | H1      | 2.5rem | 40px     |
    | H2      | 1.75rem| 28px     |
    | H3      | 1.25rem| 20px     |
    | BODY    | 1rem   | 16px     |
    | SMALL   | 0.875rem| 14px    |
    | MICRO   | 0.75rem| 12px     |
    """

    DISPLAY: str = "3.5rem"
    H1: str = "2.5rem"
    H2: str = "1.75rem"
    H3: str = "1.25rem"
    BODY: str = "1rem"
    SMALL: str = "0.875rem"
    MICRO: str = "0.75rem"


# --- Tamaños responsive del wordmark ---
WORDMARK_SIZE_DESKTOP: str = "48px"
WORDMARK_SIZE_MOBILE: str = "32px"
