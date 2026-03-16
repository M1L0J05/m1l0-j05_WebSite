"""Template — Layout base SPA de milo-jos.es.

Envuelve el contenido de cada página con: navbar + contenido + footer.
Inyecta los keyframes CSS globales y los estilos de animación.

Especificaciones: docs/architecture.md > Templates
"""

import reflex as rx

from milo_jos.components.navbar import navbar
from milo_jos.components.footer import footer
from milo_jos.styles import Color, get_all_keyframes


def template(content: rx.Component) -> rx.Component:
    """Layout base que envuelve todo el contenido de la página.

    Incluye:
    - Inyección de keyframes CSS globales
    - Navbar sticky
    - Contenido principal (secciones)
    - Footer

    Args:
        content: Componente(s) hijo(s) que forman el cuerpo de la página.

    Returns:
        Layout completo de la página.
    """
    return rx.box(
        # Inyección de keyframes CSS globales
        rx.html(f"<style>{get_all_keyframes()}</style>"),
        # Navbar
        navbar(),
        # Contenido principal
        rx.box(
            content,
            width="100%",
            min_height="100vh",
            flex="1",
        ),
        # Footer
        footer(),
        # Estilos del contenedor raíz
        display="flex",
        flex_direction="column",
        min_height="100vh",
        width="100%",
        background_color=Color.BG_BASE,
    )
