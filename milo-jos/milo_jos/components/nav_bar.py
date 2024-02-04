import reflex as rx

from milo_jos.styles.styles import Size
from milo_jos.styles.colors import Colors
from milo_jos.styles.styles import CUSTOM_BOX_STYLES


def navbar():
    return rx.hstack(
        rx.link(
            rx.hstack(
                rx.image(
                    src="mj_logo.png",
                    max_width='75px', 
                    height="auto",
                ),
                rx.text(
                    " m1l0_j05!",
                    font_size=Size.BIG.value,
                    color=Colors.PRIMARY.value,
                ),
                padding=Size.VERY_SMALL.value,
            ),
            href='/'
        ),
        rx.spacer(),
        rx.hstack(
            rx.tooltip(
                rx.square(
                    rx.icon(
                        tag='hamburger',
                        color='#CB91E5',
                        style=CUSTOM_BOX_STYLES,
                        width=Size.VERY_BIG.value,
                        height=Size.VERY_BIG.value,
                        padding=Size.SMALL.value,
                    ),
                    display=['flex', 'none', 'none', 'none', 'none', 'none'],
                ),
                label='Work In Progress'
            ),
            rx.link(
                'Home',
                href='/',
                display=['none', 'flex','flex','flex','flex', 'flex'],
            ),
            rx.tooltip(
                rx.link(
                    'Proyectos',
                    display=['none', 'flex','flex','flex','flex', 'flex'],
                ),
                label='Work In Progress'
            ),
            rx.tooltip(
                rx.link(
                    'Blog',
                    display=['none', 'flex','flex','flex','flex', 'flex'],
                ),
                label='Work In Progress'
            ),
        ),

        position="fixed",
        width="100%",
        top="0px",
        z_index="1000",
        padding_y=Size.SMALL.value,
        padding_x=Size.LARGE.value,
    )