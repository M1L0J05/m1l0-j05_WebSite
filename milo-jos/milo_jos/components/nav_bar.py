import reflex as rx

from milo_jos.styles.styles import Size
from milo_jos.styles.colors import Colors
from milo_jos.styles.styles import CUSTOM_BOX_STYLES


def navbar():
    return rx.hstack(
        rx.link(
            rx.hstack(
                rx.image(
                    src='/images/mj_logo.png',
                    max_width='75px', 
                    height='auto',
                ),
                rx.text(
                    ' m1l0_j05!',
                    font_size=Size.BIG.value,
                    color=Colors.PRIMARY.value,
                ),
                padding=Size.VERY_SMALL.value,
                align='center',
            ),
            href='/'
        ),
        rx.spacer(),
        rx.box(
            rx.menu.root(
                rx.menu.trigger(
                    rx.icon(
                        tag='menu',
                        color='#CB91E5',
                        style=CUSTOM_BOX_STYLES,
                        width=Size.VERY_BIG.value,
                        height=Size.VERY_BIG.value,
                        padding=Size.SMALL.value,
                    ),
                ),
                rx.menu.content(
                    rx.menu.item(
                        rx.link(
                            'Inicio',
                            href='/',
                            color=Colors.ACCENT.value,
                        ),
                    ),
                    rx.menu.item(
                        rx.link(
                            'Sobre mi',
                            href='/about_me',
                            color=Colors.ACCENT.value,
                        ),
                    ),
                    rx.menu.item(
                        rx.link(
                            'Proyectos',
                            href='/projects',
                            color=Colors.ACCENT.value,
                        ),
                    ),
                    background_color=Colors.BODY_BACKGROUND.value,
                    border_color=Colors.PRIMARY.value,
                    border_radius='1em',
                    border_width='1px',
                ), 
            ),
            display=['flex', 'flex', 'none', 'none', 'none', 'none'],
        ),

        rx.hstack(
            rx.link(
                'Inicio',
                href='/',
            ),
            rx.link(
                'Sobre Mi',
                href='/about_me',
            ),
            rx.link(
                'Proyectos',
                href='/projects',
            ),
            display=['none', 'none','flex','flex','flex', 'flex'],
        ),

        position='fixed',
        width='100%',
        top='0px',
        z_index='1000',
        align='center',
        padding_y=Size.SMALL.value,
        padding_x=Size.LARGE.value,
    )