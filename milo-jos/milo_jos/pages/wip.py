import reflex as rx

from milo_jos.templates import template
from milo_jos.styles.styles import *
from milo_jos.styles.colors import Colors


#Variables
texto1 = 'Este espacio del WebSite esta en proceso de construcción, ruego disculpe las molestias.'

@template(route='/wip', title='m1l0_j05 WebSite')
def wip() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.vstack(
                rx.avatar(
                    src='/images/temp/wip.svg',
                    min_height='512px',
                    width='auto',
                    border_width='3px',
                    border_color=Colors.PRIMARY.value,
                ),
                rx.spacer(),
                rx.vstack(
                    rx.text('Espacio'),
                    rx.text('en'),
                    rx.text('Construcción'),
                    color=Colors.PRIMARY.value,
                    font_size=Size.BIG.value,
                    margin_y=Size.DEFAULT.value,
                    display=['flex', 'flex', 'none', 'none', 'none', 'none'],
                ),
                rx.text(
                    'Espacio en Construcción', 
                    color=Colors.PRIMARY.value,
                    font_size=Size.VERY_BIG.value,
                    margin_y=Size.DEFAULT.value,
                    display=['none', 'none','flex','flex','flex', 'flex'],
                ),
            ),
            rx.divider(
                border_color=Colors.ACCENT.value
            ),
            rx.vstack(
                rx.text(
                    texto1,
                    color=Colors.CONTENT.value,
                    font_size='1.3em',
                    text_align = 'justify',
                    text_justify = 'inter-word'
                ),
                margin_y=Size.VERY_BIG.value,

            ),
            rx.divider(
                border_color=Colors.ACCENT.value
            ),
            #rx.vstack(    
            #    rx.box(
            #        "This is a test text...",
            #        color='#DADADE',
            #    ),
            #    rx.box(
            #        "This is a test text...",
            #        color='grey',
            #    ),
            #    rx.link(
            #        "Check out our docs!",
            #        color='#CB91E5',
            #        border="0.1em solid #335DB8",
            #        padding="0.5em",
            #        border_radius="0.5em",
            #        _hover={
            #            "color": "#DADADE",
            #            "border" : "0.1em solid #4EA0ED",
            #        },
            #    ),
            #),

            width='95%',
            padding=Size.LARGE.value,
            border_radius=Size.SMALL.value,
            min_width=MIN_WIDTH,
            max_width=MAX_WIDTH,
        ),
    )