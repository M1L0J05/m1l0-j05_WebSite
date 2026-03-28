"""Constantes de la aplicación milo-jos.es.

Centraliza valores estáticos reutilizados en múltiples módulos:
URLs, textos de identidad, metadatos SEO, links sociales.
"""

from milo_jos.version import __version__

# =============================================================================
# Identidad / Marca
# =============================================================================

SITE_NAME: str = "m1l0_j05"
SITE_DOMAIN: str = "milo-jos.es"
SITE_URL: str = f"https://{SITE_DOMAIN}"

# Variantes del wordmark (ver docs/identity-system.md)
WORDMARK_HERO: str = ">_m1l0_j05"
WORDMARK_NAVBAR: str = "m1l0_j05"
WORDMARK_FOOTER: str = "m1l0_j05"
WORDMARK_SHORT: str = "m1l0"

# Taglines
TAGLINE_HERO: str = "Building systems. Automating the rest."
TAGLINE_SEO: str = (
    "Full-Stack Engineer · DevOps · Infrastructure Architect"
)
TAGLINE_BIO: str = (
    "I build the backend, the infra, and the pipelines that run on top."
)

# UVP (Unique Value Proposition)
UVP: str = (
    "Desarrollador Full‑Stack, especializado en backend e infraestructura. "
    "Diseño y construyo sistemas completos: desde la aplicación hasta la automatización y orquestación de servicios."
    "Trabajo con Python, contenedores, virtualización y automatización para crear infraestructuras "
    "sólidas y pipelines eficientes que funcionan en cloud y on‑premise."
)

# =============================================================================
# SEO / Meta
# =============================================================================

META_TITLE: str = f"{SITE_NAME} — {TAGLINE_SEO}"
META_DESCRIPTION: str = UVP
META_OG_IMAGE: str = f"{SITE_URL}/images/root/og-image.png"

# =============================================================================
# Links sociales
# =============================================================================

GITHUB_URL: str = "https://github.com/M1L0J05"
TELEGRAM_URL: str = "https://t.me/M1L0J05"

SOCIAL_LINKS: list[dict[str, str]] = [
    {"name": "GitHub", "url": GITHUB_URL, "icon": "github"},
    {"name": "Telegram (@M1L0J05)", "url": TELEGRAM_URL, "icon": "send"},
]

# =============================================================================
# Contacto
# =============================================================================

EMAIL: str = "contacto@milo-jos.es"
AVAILABILITY_BADGE: str = "Abierto a proyectos freelance"

# =============================================================================
# Navegación (anclas SPA)
# =============================================================================

NAV_ITEMS: list[dict[str, str]] = [
    {"label": "Stack", "href": "#stack"},
    {"label": "Proyectos", "href": "#proyectos"},
    {"label": "Sobre Mí", "href": "#sobre-mi"},
]

# =============================================================================
# Footer
# =============================================================================

COPYRIGHT_YEAR_START: int = 2023
FOOTER_VERSION: str = f"v{__version__}"
