"""Página de detalle de proyecto — Ruta dinámica /proyectos/[id].

Carga los datos del proyecto desde ``assets/data/projects.json`` y renderiza
una vista editorial completa con: sección hero, grid de overview asimétrico,
panel de stack tecnológico y CTA de siguiente proyecto.

Diseño adaptado del template editorial en ``tests/code.txt``.

Ruta: /proyectos/[id]
"""

import reflex as rx

from milo_jos.templates import template
from milo_jos.sections.projects import load_projects
from milo_jos.styles import (
    Color,
    GlassBg,
    FontFamily,
    FontSize,
    FontWeight,
    GLASS_CARD,
    HEADING_STYLE,
    SECTION_PADDING,
    CONTAINER_MAX_WIDTH,
)
from milo_jos.components import secondary_button


# Datos precargados en tiempo de build. El orden de inserción (Python 3.7+)
# permite navegación circular sin estado adicional.
_PROJECTS_BY_ID: dict[str, dict] = {
    p["id"]: p for p in load_projects()
}
_PROJECTS_LIST: list[dict] = list(_PROJECTS_BY_ID.values())

# Padding horizontal compartido entre secciones (responsive)
_PX: list[str] = SECTION_PADDING["padding_x"]


class ProjectDetailState(rx.State):
    """Estado para la página de detalle de proyecto.

    Expone vars computados para los datos del proyecto actual y del
    siguiente en la lista (circular), listos para uso en el template.
    """

    @rx.var
    def project(self) -> dict:
        """Diccionario del proyecto actual o vacío si no existe."""
        # Extraer el id dinámico inyectado por el router de Reflex
        project_id: str = self.router._page.params.get("id", "")
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
        """Estado del proyecto (PRODUCCIÓN, EN DESARROLLO, etc.)."""
        return self.project.get("status", "")

    @rx.var
    def project_tech_stack(self) -> list[str]:
        """Lista de tecnologías del stack."""
        return self.project.get("tech_stack", [])

    @rx.var
    def project_image(self) -> str:
        """Ruta a la imagen hero del proyecto (cadena vacía si no hay)."""
        return self.project.get("image") or ""

    @rx.var
    def project_demo_url(self) -> str:
        """URL de demo pública (cadena vacía si no existe)."""
        return self.project.get("demo_url") or ""

    @rx.var
    def project_repo_url(self) -> str:
        """URL del repositorio (cadena vacía si es privado o no existe)."""
        return self.project.get("repo_url") or ""

    @rx.var
    def project_found(self) -> bool:
        """True si el proyecto fue encontrado en el índice."""
        return bool(self.project)

    @rx.var
    def has_demo(self) -> bool:
        """True si el proyecto tiene URL de demo pública."""
        return bool(self.project.get("demo_url"))

    @rx.var
    def has_repo(self) -> bool:
        """True si el proyecto tiene URL de repositorio público."""
        return bool(self.project.get("repo_url"))

    @rx.var
    def next_project_name(self) -> str:
        """Nombre del siguiente proyecto en la lista (circular)."""
        project_id: str = self.router._page.params.get("id", "")
        for i, p in enumerate(_PROJECTS_LIST):
            if p["id"] == project_id:
                return _PROJECTS_LIST[(i + 1) % len(_PROJECTS_LIST)].get("name", "")
        return _PROJECTS_LIST[0].get("name", "") if _PROJECTS_LIST else ""

    @rx.var
    def next_project_href(self) -> str:
        """Href del siguiente proyecto en la lista (circular)."""
        project_id: str = self.router._page.params.get("id", "")
        for i, p in enumerate(_PROJECTS_LIST):
            if p["id"] == project_id:
                return _PROJECTS_LIST[(i + 1) % len(_PROJECTS_LIST)].get("href", "/")
        return _PROJECTS_LIST[0].get("href", "/") if _PROJECTS_LIST else "/"

    @rx.var
    def next_project_image(self) -> str:
        """Imagen del siguiente proyecto (cadena vacía si no tiene)."""
        project_id: str = self.router._page.params.get("id", "")
        for i, p in enumerate(_PROJECTS_LIST):
            if p["id"] == project_id:
                return _PROJECTS_LIST[(i + 1) % len(_PROJECTS_LIST)].get("image") or ""
        return _PROJECTS_LIST[0].get("image") or "" if _PROJECTS_LIST else ""


# =============================================================================
# Helpers de estilo dinámico para el badge de estado
# =============================================================================

def _status_text_color(status: rx.Var) -> rx.Var:
    """Color de texto según el estado del proyecto.

    Args:
        status: Var con el string del estado.

    Returns:
        Var de color semántico (verde / cian / naranja).
    """
    # Verde = producción, cian = desarrollo, naranja = resto (lab, beta, etc.)
    return rx.cond(
        status == "PRODUCCIÓN",
        Color.ACCENT_GREEN,
        rx.cond(
            status == "EN DESARROLLO",
            Color.ACCENT_CYAN,
            Color.ACCENT_ORANGE,
        ),
    )


def _status_bg_color(status: rx.Var) -> rx.Var:
    """Fondo semitransparente para el badge de estado.

    Args:
        status: Var con el string del estado.

    Returns:
        Var con valor RGBA de fondo.
    """
    return rx.cond(
        status == "PRODUCCIÓN",
        "rgba(63, 185, 80, 0.12)",
        rx.cond(
            status == "EN DESARROLLO",
            GlassBg.ACCENT_CYAN_10,
            "rgba(255, 107, 43, 0.12)",
        ),
    )


def _status_border_color(status: rx.Var) -> rx.Var:
    """Borde para el badge de estado.

    Args:
        status: Var con el string del estado.

    Returns:
        Var con propiedad CSS border completa.
    """
    return rx.cond(
        status == "PRODUCCIÓN",
        "1px solid rgba(63, 185, 80, 0.3)",
        rx.cond(
            status == "EN DESARROLLO",
            f"1px solid {GlassBg.ACCENT_CYAN_30}",
            "1px solid rgba(255, 107, 43, 0.3)",
        ),
    )


# =============================================================================
# Secciones de la página
# =============================================================================

def _status_badge_dynamic() -> rx.Component:
    """Badge de estado con colores calculados en tiempo de ejecución.

    Versión dinámica (usa Vars) necesaria para la página de detalle
    donde el estado viene del router y no puede evaluarse en build time.

    Returns:
        Texto estilizado como badge con colores semánticos.
    """
    return rx.text(
        ProjectDetailState.project_status,
        font_family=FontFamily.MONO,
        font_size=FontSize.MICRO,
        font_weight=FontWeight.BOLD,
        text_transform="uppercase",
        letter_spacing="0.1em",
        color=_status_text_color(ProjectDetailState.project_status),
        background=_status_bg_color(ProjectDetailState.project_status),
        border=_status_border_color(ProjectDetailState.project_status),
        border_radius="6px",
        padding_x="0.75rem",
        padding_y="0.375rem",
        display="inline-block",
        width="fit-content",
    )


def _hero_section() -> rx.Component:
    """Sección hero con imagen de fondo full-bleed, gradient y título.

    La imagen ocupa toda la caja; un gradient de abajo hacia arriba asegura
    legibilidad del título. Si no hay imagen se usa un fondo degradado.

    Returns:
        Box relativo con imagen, overlay y nombre del proyecto superpuesto.
    """
    return rx.box(
        # Imagen de fondo o degradado fallback
        rx.cond(
            ProjectDetailState.project_image != "",
            rx.image(
                src=ProjectDetailState.project_image,
                width="100%",
                height="100%",
                object_fit="cover",
                object_position="center center",
                alt=ProjectDetailState.project_name,
                position="absolute",
                top="0",
                left="0",
            ),
            rx.box(
                width="100%",
                height="100%",
                background=(
                    f"linear-gradient(135deg, {Color.BG_CARD} 0%, {Color.BG_ELEVATED} 100%)"
                ),
                position="absolute",
                top="0",
                left="0",
            ),
        ),
        # Gradient overlay para legibilidad del título
        rx.box(
            position="absolute",
            top="0",
            left="0",
            right="0",
            bottom="0",
            background=(
                f"linear-gradient(to top, {Color.BG_BASE} 5%, "
                "rgba(13,17,23,0.65) 45%, rgba(13,17,23,0.1) 100%)"
            ),
            pointer_events="none",
        ),
        # Botón volver + título: centrado dentro de CONTAINER_MAX_WIDTH
        # igual que el resto de secciones para alineación horizontal coherente
        rx.box(
            rx.box(
                secondary_button("← Volver", href="/#proyectos"),
                rx.heading(
                    ProjectDetailState.project_name,
                    as_="h1",
                    font_family=FontFamily.HEADING,
                    font_weight=FontWeight.EXTRA_BOLD,
                    color=Color.TEXT_PRIMARY,
                    font_size=["1.75rem", "2.5rem", "3.5rem", "4.5rem"],
                    line_height="1.1",
                    margin_top="1.25rem",
                    text_shadow="0 2px 24px rgba(0,0,0,0.9)",
                ),
                max_width=CONTAINER_MAX_WIDTH,
                margin_x="auto",
                padding_x=_PX,
            ),
            position="absolute",
            bottom="2.5rem",
            left="0",
            right="0",
            width="100%",
        ),
        position="relative",
        width="100%",
        # Altura aumentada en desktop para mostrar más de la imagen
        height=["280px", "400px", "540px", "620px"],
        overflow="hidden",
        background_color=Color.BG_CARD,
    )


def _divider() -> rx.Component:
    """Separador horizontal sutil.

    Returns:
        Línea horizontal de 1px con opacidad reducida.
    """
    return rx.box(
        width="100%",
        height="1px",
        background=Color.BORDER,
        opacity="0.45",
        flex_shrink="0",
    )


def _meta_field(label: str, content: rx.Component) -> rx.Component:
    """Campo de metadata con label y contenido.

    Args:
        label: Etiqueta en mayúsculas (texto estático).
        content: Componente con el valor del campo.

    Returns:
        VStack con label y contenido alineados a la izquierda.
    """
    return rx.vstack(
        rx.text(
            label,
            font_family=FontFamily.MONO,
            font_size="0.65rem",
            text_transform="uppercase",
            letter_spacing="0.18em",
            color=Color.TEXT_SECONDARY,
            font_weight=FontWeight.BOLD,
        ),
        content,
        spacing="1",
        align_items="flex-start",
        width="100%",
    )


def _overview_section() -> rx.Component:
    """Grid asimétrico: descripción larga (izq) + sidebar de metadata (dcha).

    En desktop usa proporción 2:1 (descripción : sidebar).
    En mobile se colapsa a columna única.

    Returns:
        Grid responsive con descripción y panel de metadatos del proyecto.
    """
    # --- Sidebar: contenido de cada campo ---
    demo_content = rx.cond(
        ProjectDetailState.has_demo,
        rx.link(
            "Ver demo →",
            href=ProjectDetailState.project_demo_url,
            is_external=True,
            font_family=FontFamily.HEADING,
            font_size=FontSize.BODY,
            font_weight=FontWeight.SEMI_BOLD,
            color=Color.ACCENT_CYAN,
            underline="none",
            _hover={"text_decoration": "underline"},
        ),
        rx.text(
            "—",
            font_family=FontFamily.HEADING,
            font_size=FontSize.BODY,
            font_weight=FontWeight.SEMI_BOLD,
            color=Color.TEXT_SECONDARY,
        ),
    )

    repo_content = rx.cond(
        ProjectDetailState.has_repo,
        rx.link(
            "Ver código →",
            href=ProjectDetailState.project_repo_url,
            is_external=True,
            font_family=FontFamily.HEADING,
            font_size=FontSize.BODY,
            font_weight=FontWeight.SEMI_BOLD,
            color=Color.ACCENT_CYAN,
            underline="none",
            _hover={"text_decoration": "underline"},
        ),
        rx.text(
            "Privado",
            font_family=FontFamily.HEADING,
            font_size=FontSize.BODY,
            font_weight=FontWeight.SEMI_BOLD,
            color=Color.TEXT_SECONDARY,
        ),
    )

    status_content = rx.text(
        ProjectDetailState.project_status,
        font_family=FontFamily.HEADING,
        font_size=FontSize.BODY,
        font_weight=FontWeight.SEMI_BOLD,
        color=Color.TEXT_PRIMARY,
    )

    return rx.box(
        rx.grid(
            # Columna principal: badge de estado + descripción
            rx.vstack(
                _status_badge_dynamic(),
                rx.text(
                    ProjectDetailState.project_description,
                    font_family=FontFamily.BODY,
                    font_size=["1rem", "1.05rem", "1.1rem"],
                    color=Color.TEXT_SECONDARY,
                    line_height="1.85",
                ),
                spacing="5",
                align_items="flex-start",
                width="100%",
            ),
            # Sidebar: panel glass con metadata
            rx.box(
                rx.vstack(
                    _meta_field("Estado", status_content),
                    _divider(),
                    _meta_field("Demo", demo_content),
                    _divider(),
                    _meta_field("Repositorio", repo_content),
                    spacing="4",
                    width="100%",
                    align_items="flex-start",
                    padding="1.75rem",
                ),
                **GLASS_CARD,
                width="100%",
                align_self="start",
                _hover={
                    "box_shadow": f"0 0 20px {GlassBg.GLOW_CYAN}",
                    "transform": "translateY(-4px)",
                },
                transition="box-shadow 0.3s ease, transform 0.3s ease",
            ),
            # Grid responsive: 1 col (mobile) → 2:1 (desktop)
            grid_template_columns=rx.breakpoints(
                initial="1fr",
                lg="2fr 1fr",
            ),
            gap=["2rem", "2.5rem", "3rem"],
            width="100%",
            align_items="start",
        ),
        padding_x=_PX,
        padding_y="3.5rem",
        max_width=CONTAINER_MAX_WIDTH,
        width="100%",
        margin_x="auto",
    )


def _tech_stack_section() -> rx.Component:
    """Panel centrado con las tecnologías del stack del proyecto.

    Usa rx.foreach para renderizar un badge por cada tecnología.

    Returns:
        Box con panel glass y flex grid de chips de tecnología.
    """
    return rx.box(
        rx.box(
            # Título del panel
            rx.text(
                "La Fuerza Bajo La Interfaz",
                font_family=FontFamily.HEADING,
                font_size=FontSize.H2,
                font_weight=FontWeight.BOLD,
                color=Color.TEXT_PRIMARY,
                text_align="center",
                margin_bottom="2rem",
            ),
            # Chips de cada tecnología generados con foreach
            rx.flex(
                rx.foreach(
                    ProjectDetailState.project_tech_stack,
                    lambda tech: rx.text(
                        tech,
                        font_family=FontFamily.MONO,
                        font_size=FontSize.MICRO,
                        text_transform="uppercase",
                        letter_spacing="0.08em",
                        color=Color.ACCENT_CYAN,
                        background=GlassBg.ACCENT_CYAN_10,
                        border=f"1px solid {GlassBg.ACCENT_CYAN_30}",
                        border_radius="8px",
                        padding_x="1.25rem",
                        padding_y="0.625rem",
                        _hover={
                            "border_color": GlassBg.ACCENT_CYAN_60,
                            "transform": "scale(1.05)",
                        },
                        transition="border-color 0.2s ease, transform 0.2s ease",
                        cursor="default",
                        white_space="nowrap",
                    ),
                ),
                justify="center",
                wrap="wrap",
                gap="0.5rem",
            ),
            **GLASS_CARD,
            padding=["1.75rem", "2rem", "2.5rem"],
            _hover={
                "box_shadow": f"0 0 20px {GlassBg.GLOW_CYAN}",
                "transform": "translateY(-4px)",
            },
            transition="box-shadow 0.3s ease, transform 0.3s ease",
        ),
        padding_x=_PX,
        padding_bottom="3.5rem",
        max_width=CONTAINER_MAX_WIDTH,
        width="100%",
        margin_x="auto",
    )


def _next_project_section() -> rx.Component:
    """CTA de navegación al siguiente proyecto — card full-width.

    La tarjeta usa la imagen del siguiente proyecto como fondo,
    con un overlay oscuro y el nombre centrado. Navega de forma
    circular (el último proyecto enlaza al primero).

    Returns:
        Link-card con imagen, overlay semitransparente y título del proyecto.
    """
    return rx.box(
        rx.link(
            rx.box(
                # Imagen de fondo del siguiente proyecto
                rx.image(
                    src=ProjectDetailState.next_project_image,
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    alt=ProjectDetailState.next_project_name,
                    position="absolute",
                    top="0",
                    left="0",
                ),
                # Overlay oscuro semitransparente
                rx.box(
                    position="absolute",
                    top="0",
                    left="0",
                    right="0",
                    bottom="0",
                    background="rgba(0, 0, 0, 0.65)",
                    transition="background 0.3s ease",
                    border_radius="inherit",
                ),
                # Contenido centrado verticalmente
                rx.vstack(
                    rx.text(
                        "Siguiente Proyecto",
                        font_family=FontFamily.MONO,
                        font_size=FontSize.MICRO,
                        font_weight=FontWeight.REGULAR,
                        text_transform="uppercase",
                        letter_spacing="0.05em",
                        color=Color.ACCENT_GREEN,
                        background="rgba(63, 185, 80, 0.1)",
                        border="1px solid rgba(63, 185, 80, 0.3)",
                        border_radius="6px",
                        padding_x="0.75rem",
                        padding_y="0.375rem",
                        white_space="nowrap",
                    ),
                    rx.heading(
                        ProjectDetailState.next_project_name,
                        font_family=FontFamily.HEADING,
                        font_weight=FontWeight.EXTRA_BOLD,
                        font_size=["1.75rem", "2.5rem", "3.5rem"],
                        color=Color.TEXT_PRIMARY,
                        text_align="center",
                        line_height="1.1",
                    ),
                    rx.hstack(
                        rx.text(
                            "Ver proyecto",
                            font_family=FontFamily.HEADING,
                            font_size=FontSize.SMALL,
                            font_weight=FontWeight.BOLD,
                            text_transform="uppercase",
                            letter_spacing="0.12em",
                            color=Color.ACCENT_CYAN,
                        ),
                        rx.icon(
                            "arrow-right",
                            size=18,
                            color=Color.TEXT_PRIMARY,
                        ),
                        spacing="2",
                        align="center",
                    ),
                    spacing="4",
                    align="center",
                    position="absolute",
                    top="50%",
                    left="50%",
                    transform="translate(-50%, -50%)",
                    text_align="center",
                    width="80%",
                ),
                position="relative",
                width="100%",
                height=["250px", "300px", "400px"],
                overflow="hidden",
                border_radius="12px",
                background_color=Color.BG_CARD,
                _hover={
                    "box_shadow": f"0 0 40px {GlassBg.GLOW_CYAN}",
                    "transform": "scale(1.005)",
                },
                transition="box-shadow 0.3s ease, transform 0.3s ease",
            ),
            href=ProjectDetailState.next_project_href,
            underline="none",
            display="block",
            width="100%",
        ),
        padding_x=_PX,
        padding_bottom="5rem",
        max_width=CONTAINER_MAX_WIDTH,
        width="100%",
        margin_x="auto",
    )


def _project_not_found() -> rx.Component:
    """Vista cuando el proyecto no existe.

    Returns:
        Mensaje de error centrado con enlace para volver al inicio.
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
    """Vista editorial completa del proyecto.

    Compone las cuatro secciones en orden: hero, overview,
    stack tecnológico y CTA de siguiente proyecto.

    Returns:
        VStack con todas las secciones de la página de detalle.
    """
    return rx.vstack(
        _hero_section(),
        _overview_section(),
        _tech_stack_section(),
        _next_project_section(),
        spacing="0",
        width="100%",
        align_items="stretch",
    )


# Mismo fondo que el hero de la home: patrón circuit-board + gradiente oscuro
_PAGE_BG_GRADIENT: str = (
    f"linear-gradient(135deg, {Color.BG_BASE} 0%, #0a1628 25%, "
    f"{Color.BG_BASE} 50%, #0d1f2d 75%, {Color.BG_BASE} 100%)"
)
_PAGE_BACKGROUND: str = f"url('/images/root/circuit-board.svg'), {_PAGE_BG_GRADIENT}"


def project_detail() -> rx.Component:
    """Página de detalle de un proyecto individual.

    Muestra la vista editorial si el proyecto existe,
    o un mensaje de error si no se encuentra.

    El fondo replica el patrón circuit-board + gradiente del hero principal.

    Returns:
        Layout completo con template (navbar + contenido + footer).
    """
    return template(
        rx.box(
            rx.cond(
                ProjectDetailState.project_found,
                _project_detail_view(),
                rx.box(
                    _project_not_found(),
                    width="100%",
                    display="flex",
                    justify_content="center",
                    padding_x=_PX,
                ),
            ),
            width="100%",
            # Fondo coherente con la home
            background_image=_PAGE_BACKGROUND,
            background_size="250px 250px, 100% 100%",
            background_repeat="repeat, no-repeat",
            background_attachment="fixed",
        )
    )
