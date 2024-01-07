import reflex as rx

from milo_jos.templates import template


@template(route='/', title='miloJosWeb')
def index() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.heading(
                "Welcome to MiloJos_Web!", 
                color='#335DB8',
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
        ),
    )