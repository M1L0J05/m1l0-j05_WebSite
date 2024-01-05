from typing import Callable

import reflex as rx

# Etiquetas metadatos para la aplicacion
default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1",
    },
]

def template(
    route: str | None = None,
    title: str | None = None,
    image: str | None = None,
    description: str | None = None,
    meta: str | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.event.EventHandler | list[rx.event.EventHandler] | None = None,
) -> rx.Component:
    """ La plantilla para cada página de la aplicación.

     Argumentos:
         route: La ruta para llegar a la página.
         title: El título de la página.
         image: El favicon de la página.
         description: La descripción de la página.
         meta: Metadatos adicional para agregar a la página.
         script_tags: Scripts para adjuntar a la página.
         on_load: Los controladores de eventos llamados cuando se carga la página.

     Retorna:
         La plantilla con el contenido de la página.
    """
    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        """La plantilla para cada página de la aplicación.

        Argumentos:
            page_content: El contenido de la página.
        
        Retorna:
            La plantilla con el contenido de la página.
        """
        # Obtener las etiquetas de metadatos de la página.
        all_meta = [*default_meta, *(meta or [])]

        # Este decorador es imprescindible para que la aplicacion entieda que se trata de una página
        @rx.page(
            route=route,
            title=title,
            image=image,
            description=description,
            meta=all_meta,
            script_tags=script_tags,
            on_load=on_load,
        ) 
        # Renderizado de la plantilla junto con el contenido de la página.
        def templated_page() -> rx.Component:
            return rx.hstack(
                rx.heading("Plantilla - Header", font_size="2em"),
                page_content(),
                rx.heading("Plantilla - Footer", font_size="2em"),
            )

        return templated_page

    return decorator
        