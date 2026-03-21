"""Sección Proyectos — Carrusel horizontal con scroll-snap.

Carga la lista de proyectos desde el fichero JSON estático en tiempo
de build y genera un carrusel horizontal de ``project_card`` con
flechas de navegación y dots indicadores de posición.

Especificaciones: docs/architecture.md > Secciones > Proyectos
"""

import json
from pathlib import Path

import reflex as rx

from milo_jos.styles import (
    Color,
    FontFamily,
    FontSize,
    HEADING_STYLE,
    SECTION_PADDING,
    SECTION_REVEAL,
    CONTAINER_MAX_WIDTH,
)
from milo_jos.components import project_card
from milo_jos.states.carousel_state import CarouselState, TOTAL_CARDS

# Ruta absoluta al JSON de proyectos (relativa al fichero actual).
_PROJECTS_JSON_PATH: Path = (
    Path(__file__).resolve().parents[2] / "assets" / "data" / "projects.json"
)

# ID del contenedor HTML del carrusel para scroll programático.
_CAROUSEL_ID: str = "projects-carousel"


def load_projects() -> list[dict]:
    """Carga y devuelve la lista de proyectos desde el fichero JSON.

    Lee ``assets/data/projects.json`` y lo parsea como lista de diccionarios.
    Si el fichero no existe, devuelve una lista vacía para evitar errores
    en tiempo de build.

    Returns:
        Lista de diccionarios con los datos de cada proyecto.
    """
    try:
        data = _PROJECTS_JSON_PATH.read_text(encoding="utf-8")
        return json.loads(data)
    except FileNotFoundError:
        return []


def _build_project_card(project: dict) -> rx.Component:
    """Construye una tarjeta de proyecto a partir de un diccionario.

    Extrae los campos necesarios del diccionario y los pasa como
    argumentos con nombre a ``project_card``. El campo ``image`` solo
    se incluye si existe y no es nulo.

    Args:
        project: Diccionario con los datos de un proyecto individual.

    Returns:
        Componente ``project_card`` configurado.
    """
    # Preparar kwargs base
    kwargs: dict = {
        "name": project["name"],
        "description": project["description"],
        "status": project["status"],
        "tech_stack": project["tech_stack"],
        "href": project["href"],
    }

    # Incluir imagen solo si existe y no es nula
    image = project.get("image")
    if image:
        kwargs["image_src"] = image

    return project_card(**kwargs)


def _card_wrapper(card: rx.Component) -> rx.Component:
    """Envuelve una tarjeta en un contenedor de ancho fijo para el carrusel.

    Aplica ``scroll_snap_align`` para que el scroll se detenga en cada
    tarjeta y ``flex_shrink="0"`` para evitar que flex comprima el ancho.

    Args:
        card: Componente de tarjeta (project_card o coming_soon_card).

    Returns:
        Componente wrapper con dimensiones responsive.
    """
    return rx.box(
        card,
        # Mismos breakpoints que stack_section: initial/sm=1col, md=2col, lg=3col
        min_width=rx.breakpoints(
            initial="100%",
            sm="100%",
            md="calc(50% - 0.75rem)",
            lg="calc(33.333% - 1rem)",
        ),
        max_width=rx.breakpoints(
            initial="100%",
            sm="100%",
            md="calc(50% - 0.75rem)",
            lg="calc(33.333% - 1rem)",
        ),
        scroll_snap_align="start",
        flex_shrink="0",
        height="auto",
    )


def _nav_button(direction: str) -> rx.Component:
    """Botón de navegación lateral del carrusel.

    Posicionado absolutamente al lado izquierdo o derecho del carrusel.
    Oculto en mobile donde el swipe táctil es suficiente.

    Args:
        direction: ``"left"`` o ``"right"``.

    Returns:
        Componente icon_button estilizado.
    """
    is_left = direction == "left"

    return rx.icon_button(
        rx.icon("chevron_left" if is_left else "chevron_right", size=20),
        variant="ghost",
        size="3",
        on_click=CarouselState.scroll_prev if is_left else CarouselState.scroll_next,
        position="absolute",
        top="50%",
        transform="translateY(-50%)",
        left="-2.5rem" if is_left else "auto",
        right="auto" if is_left else "-2.5rem",
        z_index="10",
        background="transparent",
        color=Color.ACCENT_GREEN,
        border="none",
        border_radius="50%",
        width="2.5rem",
        height="2.5rem",
        cursor="pointer",
        _hover={
            "color": Color.ACCENT_GREEN,
            "opacity": "0.7",
            "transform": "translateY(-50%) scale(1.2)",
        },
        transition="all 0.3s ease",
        # Visible a partir de md (768px), igual que los breakpoints del grid
        display=rx.breakpoints(initial="none", sm="none", md="flex"),
    )



def _dot_indicator(index: int) -> rx.Component:
    """Punto indicador individual del carrusel.

    Cambia de tamaño y color según si corresponde al índice activo.
    Clicable para navegar directamente a ese card.

    Args:
        index: Índice del card que representa este dot.

    Returns:
        Componente box circular estilizado con estado reactivo.
    """
    return rx.box(
        width=rx.cond(
            CarouselState.active_index == index,
            "10px",
            "8px",
        ),
        height=rx.cond(
            CarouselState.active_index == index,
            "10px",
            "8px",
        ),
        border_radius="50%",
        background=rx.cond(
            CarouselState.active_index == index,
            Color.ACCENT_CYAN,
            Color.TEXT_SECONDARY,
        ),
        opacity=rx.cond(
            CarouselState.active_index == index,
            "1",
            "0.4",
        ),
        cursor="pointer",
        transition="all 0.3s ease",
        _hover={
            "opacity": "0.8",
            "transform": "scale(1.2)",
        },
        on_click=CarouselState.scroll_to(index),
    )


def _dot_indicators(total: int) -> rx.Component:
    """Fila de dots indicadores de posición del carrusel.

    Cada dot es clicable y navega al card correspondiente.
    Se sincronizan con el estado activo vía CarouselState.

    Args:
        total: Número total de cards en el carrusel.

    Returns:
        Componente hstack con los dots centrados.
    """
    return rx.hstack(
        *[_dot_indicator(i) for i in range(total)],
        spacing="2",
        justify="center",
        align="center",
        margin_top="1.5rem",
        width="100%",
    )


def projects_section() -> rx.Component:
    """Sección principal de proyectos del portfolio.

    Renderiza un encabezado con título y subtítulo, seguido de un
    carrusel horizontal con scroll-snap, flechas de navegación y
    dots indicadores de posición.

    Returns:
        Componente de sección listo para componer en la página.
    """
    # Cargar proyectos en tiempo de build
    projects = load_projects()

    # Construir lista de tarjetas envueltas en wrappers de ancho fijo
    cards: list[rx.Component] = [
        _card_wrapper(_build_project_card(project)) for project in projects
    ]

    return rx.box(
        rx.box(
            # Título de la sección
            rx.heading(
                "Proyectos",
                **HEADING_STYLE,
                font_size=FontSize.H1,
                as_="h2",
                width="100%",
                text_align="center",
            ),
            # Subtítulo descriptivo
            rx.text(
                "Sistemas que diseño, construyo y mantengo.",
                color=Color.TEXT_SECONDARY,
                font_family=FontFamily.HEADING,
                font_size=FontSize.BODY,
                margin_top="0.75rem",
                width="100%",
                text_align="center",
            ),
            # Wrapper relativo: flechas posicionadas absolutamente sobre el scroll
            rx.box(
                _nav_button("left"),
                _nav_button("right"),
                # Contenedor de scroll horizontal con snap
                rx.flex(
                    *cards,
                    direction="row",
                    gap=["1rem", "1.25rem", "1.5rem"],
                    overflow_x="auto",
                    scroll_snap_type="x mandatory",
                    # Padding vertical para que hover shadow no se recorte
                    padding_y="0.5rem",
                    width="100%",
                    id=_CAROUSEL_ID,
                    class_name="carousel-scroll-container",
                ),
                position="relative",
                width="100%",
                margin_top="2.5rem",
            ),
            # Dots indicadores de posición
            _dot_indicators(TOTAL_CARDS),
            max_width=CONTAINER_MAX_WIDTH,
            width="100%",
            margin_x="auto",
        ),
        id="proyectos",
        as_="section",
        width="100%",
        **SECTION_PADDING,
        **SECTION_REVEAL,
    )
