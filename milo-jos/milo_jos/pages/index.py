import reflex as rx

from milo_jos.templates import template
from milo_jos.styles.styles import *
from milo_jos.styles.colors import Colors, TextColors


@template(route='/', title='miloJosWeb')
def index() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading(
                "Welcome to { M1L0_J05 } !", 
                color=TextColors.DEFAULT.value,
            ),
            rx.box(
                "Get started by editing ",
                color='#335DB8',
            ),
            rx.box(
                "This is a test text...",
                color='#DADADE',
            ),
            rx.box(
                "This is a test text...",
                color='grey',
            ),
            rx.link(
                "Check out our docs!",
                color='#CB91E5',
                border="0.1em solid #335DB8",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "#DADADE",
                    "border" : "0.1em solid #4EA0ED",
                },
            ),
            #background_color=Colors.BODY_BACKGROUND.value,
            width='95%',
            min_width=MIN_WIDTH,
            max_width=MAX_WIDTH,
            
        ),
    )