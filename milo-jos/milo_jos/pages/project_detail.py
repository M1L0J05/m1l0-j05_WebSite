"""Página de detalle de proyecto — Ruta dinámica /proyectos/[id].

Carga los datos del proyecto desde ``assets/data/projects.json``
y renderiza una vista detallada con stack, descripción y enlaces.

En Reflex 0.8.6, los segmentos dinámicos como [id] se exponen
automáticamente como ``rx.State.id`` (var en el estado raíz).

Ruta: /proyectos/[id]
"""

import reflex as rx

from milo_jos.templates import template
from milo_jos.sections.projects import load_projects
from milo_jos.styles import (
    Color,
    FontFamily,
    FontSize,
    FontWeight,
    GLASS_CARD,
    HEADING_STYLE,
    SECTION_PADDING,
    CONTAINER_MAX_WIDTH,
)
from milo_jos.components import secondary_button


# Cargar proyectos en tiempo de build como índice por id
_PROJECTS_BY_ID: dict[str, dict] = {
    p["id"]: p for p in load_projects()
}


class ProjectDetailState(rx.State):
    """Estado para la página de detalle de proyecto.

    Utiliza ``rx.State.id`` (inyectado automáticamente por el router
    desde la ruta ``/proyectos/[id]``) para buscar el proyecto en
    el índice de build.
    """

    @rx.var
    def project(self) -> dict:
        """Devuelve el diccionario del proyecto actual o vacío si no existe."""
        # router.page.params deprecado en 0.8.1 pero funcional en 0.8.6
        # TODO: migrar cuando router.url exponga parámetros de ruta
        project_id: str = self.router.page.params.get("id", "")
        return _PROJECTS_BY_ID.get(project_id, {})

    @rx.var
    def project_name(self) -> str:
        """Nombre del proyecto."""
        return self.project.get("name", "Proyecto no encontrado")

    @rx.var
    def project_description(self) -> str:
        """Descripción del proyecto."""
        return self.project.get("description", "")

    @rx.var
    def project_status(self) -> str:
        """Estado del proyecto."""
        return self.project.get("status", "")

    @rx.var
    def project_tech_stack(self) -> list[str]:
        """Stack tecnológico del proyecto."""
        return self.project.get("tech_stack", [])

    @rx.var
    def project_found(self) -> bool:
        """Indica si el proyecto fue encontrado."""
        return bool(self.project)


def _project_not_found() -> rx.Component:
    """Vista cuando el proyecto no existe.

    Returns:
        Mensaje de error con enlace para volver al inicio.
    """
    return rx.vstack(
        rx.icon("file-question", size=48, color=Color.TEXT_SECONDARY),
        rx.heading(
            "Proyecto no encontrado",
            **HEADING_STYLE,
            font_size=FontSize.H2,
            as_="h1",
        ),
        rx.text(
            "El proyecto que buscas no existe o ha sido movido.",
            color=Color.TEXT_SECONDARY,
            font_size=FontSize.BODY,
        ),
        secondary_button("Volver al inicio", href="/"),
        spacing="5",
        align="center",
        padding_y="6rem",
    )


def _project_detail_view() -> rx.Component:
    """Vista principal con los datos del proyecto.

    Returns:
        Layout detallado del proyecto con título, estado, descripción y stack.
    """
    return rx.vstack(
        # Botón volver
        secondary_button("< Volver", href="/#proyectos"),
        # Cabecera: nombre + estado
        rx.hstack(
            rx.heading(
                ProjectDetailState.project_name,
                **HEADING_STYLE,
                font_size=FontSize.H1,
                as_="h1",
            ),
            rx.cond(
                ProjectDetailState.project_status != "",
                rx.box(
                    rx.text(
                        ProjectDetailState.project_status,
                        font_family=FontFamily.MONO,
                        font_size=FontSize.MICRO,
                        text_transform="uppercase",
                        letter_spacing="0.05em",
                        color=Color.ACCENT_CYAN,
                        padding_x="0.625rem",
                        padding_y="0.25rem",
                        border=f"1px solid {Color.ACCENT_CYAN}",
                        border_radius="6px",
                    ),
                ),
                rx.fragment(),
            ),
            spacing="4",
            align="center",
            wrap="wrap",
        ),
        # Descripción
        rx.box(
            rx.text(
                ProjectDetailState.project_description,
                font_family=FontFamily.BODY,
                font_size=FontSize.BODY,
                color=Color.TEXT_PRIMARY,
                line_height="1.8",
            ),
            **GLASS_CARD,
            padding="2rem",
            width="100%",
        ),
        # Stack tecnológico
        rx.vstack(
            rx.text(
                "Stack Tecnológico",
                font_family=FontFamily.HEADING,
                font_size=FontSize.H3,
                font_weight=FontWeight.SEMI_BOLD,
                color=Color.TEXT_PRIMARY,
            ),
            rx.flex(
                rx.foreach(
                    ProjectDetailState.project_tech_stack,
                    lambda tech: rx.text(
                        tech,
                        font_family=FontFamily.MONO,
                        font_size=FontSize.MICRO,
                        text_transform="uppercase",
                        letter_spacing="0.05em",
                        color=Color.ACCENT_CYAN,
                        background="rgba(0, 209, 255, 0.1)",
                        border=f"1px solid rgba(0, 209, 255, 0.3)",
                        border_radius="6px",
                        padding_x="0.625rem",
                        padding_y="0.25rem",
                        white_space="nowrap",
                    ),
                ),
                wrap="wrap",
                gap="2",
            ),
            spacing="3",
            align_items="flex-start",
            width="100%",
        ),
        spacing="6",
        align_items="flex-start",
        max_width=CONTAINER_MAX_WIDTH,
        width="100%",
    )


def project_detail() -> rx.Component:
    """Página de detalle de un proyecto individual.

    Muestra la vista de detalle si el proyecto existe,
    o un mensaje de error si no se encuentra.

    Returns:
        Layout completo con template (navbar + contenido + footer).
    """
    return template(
        rx.box(
            rx.cond(
                ProjectDetailState.project_found,
                _project_detail_view(),
                _project_not_found(),
            ),
            width="100%",
            display="flex",
            justify_content="center",
            **SECTION_PADDING,
        )
    )
