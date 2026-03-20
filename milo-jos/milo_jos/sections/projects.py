"""Sección Proyectos — Grid de tarjetas con glassmorphism.

Carga la lista de proyectos desde el fichero JSON estático en tiempo
de build y genera un grid responsive de ``project_card`` junto con
una tarjeta placeholder ``coming_soon_card`` al final.

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
from milo_jos.components import project_card, coming_soon_card

# Ruta absoluta al JSON de proyectos (relativa al fichero actual).
_PROJECTS_JSON_PATH: Path = (
    Path(__file__).resolve().parents[2] / "assets" / "data" / "projects.json"
)


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


def projects_section() -> rx.Component:
    """Sección principal de proyectos del portfolio.

    Renderiza un encabezado con título y subtítulo, seguido de un grid
    responsive con las tarjetas de todos los proyectos cargados desde
    JSON y una tarjeta ``coming_soon_card`` al final.

    Returns:
        Componente de sección listo para componer en la página.
    """
    # Cargar proyectos en tiempo de build
    projects = load_projects()

    # Construir lista de tarjetas: una por proyecto + coming soon
    cards: list[rx.Component] = [
        _build_project_card(project) for project in projects
    ]
    cards.append(coming_soon_card())

    return rx.box(
        rx.box(
            # Título de la sección
            rx.heading(
                "Proyectos",
                **HEADING_STYLE,
                font_size=FontSize.H1,
                as_="h2",
            ),
            # Subtítulo descriptivo
            rx.text(
                "Sistemas que diseño, construyo y mantengo.",
                color=Color.TEXT_SECONDARY,
                font_family=FontFamily.HEADING,
                font_size=FontSize.BODY,
                margin_top="0.75rem",
            ),
            # Grid responsive de tarjetas
            rx.grid(
                *cards,
                grid_template_columns=[
                    "1fr",
                    "1fr 1fr",
                    "1fr 1fr",
                    "repeat(3, 1fr)",
                ],
                gap=["1rem", "1.25rem", "1.5rem"],
                width="100%",
                margin_top="2.5rem",
            ),
            max_width="1400px",
            width="100%",
            margin_x="auto",
        ),
        id="proyectos",
        as_="section",
        width="100%",
        # Padding reducido en desktop para dar más espacio al grid de 3 columnas
        padding_x=["1.5rem", "2rem", "3rem", "3rem"],
        padding_y=SECTION_PADDING["padding_y"],
        **SECTION_REVEAL,
    )
