"""Estado del carrusel de proyectos.

Gestiona el índice activo para sincronizar los dots indicadores
con la posición del scroll en el carrusel horizontal.
"""

import reflex as rx

# Número total de tarjetas en el carrusel (7 proyectos).
TOTAL_CARDS: int = 7

# ID del contenedor HTML del carrusel para scroll programático.
_CAROUSEL_CONTAINER_ID: str = "projects-carousel"


class CarouselState(rx.State):
    """Estado del carrusel horizontal de proyectos.

    Attributes:
        active_index: Índice del grupo de cards actualmente visible.
    """

    active_index: int = 0

    def set_active(self, index: int) -> None:
        """Actualiza el índice activo del carrusel.

        Args:
            index: Nuevo índice activo (se clampea entre 0 y TOTAL_CARDS - 1).
        """
        self.active_index = max(0, min(index, TOTAL_CARDS - 1))

    def scroll_to(self, index: int) -> rx.event.EventSpec:
        """Navega al card en la posición indicada y actualiza el dot activo.

        Desplaza el contenedor de scroll hasta el card del índice indicado
        usando la posición offsetLeft del elemento hijo.

        Args:
            index: Índice del card destino.

        Returns:
            EventSpec con el script de scroll suave.
        """
        self.active_index = max(0, min(index, TOTAL_CARDS - 1))
        # Usar offsetLeft del hijo para un posicionamiento exacto independiente del ancho
        return rx.call_script(
            f"""
            (() => {{
                const el = document.getElementById('{_CAROUSEL_CONTAINER_ID}');
                if (!el) return;
                const card = el.children[{self.active_index}];
                if (!card) return;
                el.scrollTo({{left: card.offsetLeft - el.offsetLeft, behavior: 'smooth'}});
            }})()
            """
        )

    def scroll_next(self) -> rx.event.EventSpec:
        """Avanza al siguiente card y desplaza el carrusel.

        Returns:
            EventSpec con el script de scroll hacia adelante.
        """
        self.active_index = min(self.active_index + 1, TOTAL_CARDS - 1)
        return rx.call_script(
            f"""
            (() => {{
                const el = document.getElementById('{_CAROUSEL_CONTAINER_ID}');
                if (!el) return;
                const card = el.children[{self.active_index}];
                if (!card) return;
                el.scrollTo({{left: card.offsetLeft - el.offsetLeft, behavior: 'smooth'}});
            }})()
            """
        )

    def scroll_prev(self) -> rx.event.EventSpec:
        """Retrocede al card anterior y desplaza el carrusel.

        Returns:
            EventSpec con el script de scroll hacia atrás.
        """
        self.active_index = max(self.active_index - 1, 0)
        return rx.call_script(
            f"""
            (() => {{
                const el = document.getElementById('{_CAROUSEL_CONTAINER_ID}');
                if (!el) return;
                const card = el.children[{self.active_index}];
                if (!card) return;
                el.scrollTo({{left: card.offsetLeft - el.offsetLeft, behavior: 'smooth'}});
            }})()
            """
        )
