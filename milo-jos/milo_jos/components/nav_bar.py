import reflex as rx

from milo_jos.styles.styles import Size
from milo_jos.styles.colors import Colors

def navbar():
    return rx.hstack(
        rx.image(
            src="mj_logo.png",
            max_width='75px', 
            height="auto",
        ),
        rx.text(
            "¡¡ Bienvenido !!",
            as_='i',
            font_size=Size.BIG.value,
            color=Colors.SECONDARY.value,
        ),
        rx.spacer(),
        rx.hstack(
            rx.image(
                src='github.svg',
                max_height='2em'
            ),
            rx.image(
                src='github.svg',
                max_height='2em'
            ),
            rx.image(
                src='github.svg',
                max_height='2em'
            ),
            rx.image(
                src='github.svg',
                max_height='2em'
            ),
            rx.image(
                src='github.svg',
                max_height='2em'
            ),
            #border='1px solid #CB91E5',
            border_radius=Size.VERY_SMALL.value,
            padding=Size.SMALL.value,
        ),

        position="fixed",
        width="100%",
        top="0px",
        z_index="1000",
        padding=Size.SMALL.value,
        background_color=Colors.BODY_BACKGROUND.value,
    )