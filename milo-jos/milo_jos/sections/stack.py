"""Sección Stack Técnico — Capas tecnológicas con badges.

Muestra las cuatro capas del stack de M1L0_J05 en un grid
responsive: Frontend, Backend, Infra/DevOps y Automatización.
Cada capa se presenta como una tarjeta glassmorphism con icono,
nombre y badges de tecnología.

Especificaciones: docs/architecture.md > Secciones > Stack
"""

import reflex as rx

from milo_jos.styles import (
    Color,
    FontSize,
    GLASS_CARD,
    GLASS_CARD_HOVER,
    HEADING_STYLE,
    SUBHEADING_STYLE,
    SECTION_PADDING,
    CONTAINER_MAX_WIDTH,
)
from milo_jos.components import badge


# ─── Datos de las capas del stack ────────────────────────────────────────────

# Cada capa se define como un diccionario con nombre, icono y tecnologías
_STACK_LAYERS: list[dict] = [
    {
        "name": "Frontend",
        "icon": "monitor",
        "techs": ["Python", "Reflex", "HTML", "CSS", "JavaScript"],
    },
    {
        "name": "Backend",
        "icon": "server",
        "techs": ["Python", "FastAPI", "PostgreSQL", "Redis", "REST API"],
    },
    {
        "name": "Infra / DevOps",
        "icon": "cloud",
        "techs": [
            "Docker",
            "Kubernetes",
            "Proxmox",
            "Terraform",
            "Ansible",
            "Caddy",
        ],
    },
    {
        "name": "Automatización",
        "icon": "bot",
        "techs": ["CI/CD", "GitHub Actions", "Bash", "Python Scripts"],
    },
]


# ─── Componentes internos ────────────────────────────────────────────────────


def _layer_card(
    name: str,
    icon: str,
    techs: list[str],
) -> rx.Component:
    """Tarjeta glassmorphism para una capa del stack técnico.

    Contiene un icono, el nombre de la capa y una fila de badges
    con las tecnologías asociadas.

    Args:
        name: Nombre de la capa (ej. 'Frontend').
        icon: Nombre del icono de Lucide (ej. 'monitor').
        techs: Lista de tecnologías para mostrar como badges.

    Returns:
        Componente de tarjeta con glassmorphism y hover glow.
    """
    return rx.box(
        rx.vstack(
            rx.icon(
                tag=icon,
                size=28,
                color=Color.ACCENT_CYAN,
            ),
            rx.heading(
                name,
                **SUBHEADING_STYLE,
                font_size=FontSize.H3,
                as_="h3",
            ),
            rx.flex(
                *[badge(tech) for tech in techs],
                wrap="wrap",
                gap="2",
            ),
            spacing="4",
            align="start",
            width="100%",
        ),
        **GLASS_CARD,
        padding="1.5rem",
        _hover=GLASS_CARD_HOVER,
    )


# ─── Sección exportada ──────────────────────────────────────────────────────


def stack_section() -> rx.Component:
    """Sección de stack técnico con grid responsive de 4 capas.

    Layout responsive:
    - Móvil:      1 columna
    - Tablet sm:  1 columna
    - Tablet:     2 columnas
    - Desktop:    4 columnas

    Cada capa se renderiza como una tarjeta glassmorphism con icono,
    título y badges de tecnología.

    Returns:
        Componente de sección completo con id='stack'.
    """
    return rx.box(
        rx.vstack(
            rx.heading(
                "Stack Técnico",
                **HEADING_STYLE,
                font_size=FontSize.H1,
                as_="h2",
            ),
            rx.grid(
                *[
                    _layer_card(
                        name=layer["name"],
                        icon=layer["icon"],
                        techs=layer["techs"],
                    )
                    for layer in _STACK_LAYERS
                ],
                columns=rx.breakpoints(
                    initial="1",
                    sm="1",
                    md="2",
                    lg="4",
                ),
                spacing="5",
                width="100%",
            ),
            spacing="8",
            align="center",
            width="100%",
            max_width=CONTAINER_MAX_WIDTH,
        ),
        id="stack",
        width="100%",
        display="flex",
        justify_content="center",
        **SECTION_PADDING,
    )
