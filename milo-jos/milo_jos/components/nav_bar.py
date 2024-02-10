import reflex as rx

from milo_jos.styles.styles import Size
from milo_jos.styles.colors import Colors
from milo_jos.styles.styles import CUSTOM_BOX_STYLES


def navbar():
    return rx.hstack(
        rx.link(
            rx.hstack(
                rx.image(
                    src="/images/mj_logo.png",
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
            rx.menu(
                rx.menu_button(
                    rx.square(
                        rx.icon(
                            tag='hamburger',
                            color='#CB91E5',
                            style=CUSTOM_BOX_STYLES,
                            width=Size.VERY_BIG.value,
                            height=Size.VERY_BIG.value,
                            padding=Size.SMALL.value,
                        ),
                        display=['flex', 'flex', 'none', 'none', 'none', 'none'],
                    ),
                ),
                rx.menu_list(
                    rx.menu_item(
                        rx.link(
                            'Inicio',
                            href='/'
                        ),
                        background_color='transparent',
                    ),
                    rx.menu_item(
                        rx.link(
                            'Sobre Mi',
                            href='/about_me'
                        ),
                        background_color='transparent',
                    ),
                    rx.menu_item(
                        rx.link(
                            'Proyectos',
                            href='/wip'
                        ),
                        background_color='transparent',
                    ),
                    rx.menu_item(
                        rx.link(
                            'Blog',
                            href='/wip'
                        ),
                        background_color='transparent',
                    ),
                    rx.menu_item(
                        rx.link(
                            'Contacto',
                            href='/wip'
                        ),
                        background_color='transparent',
                    ),
                    text_color=Colors.ACCENT.value,
                    background_color=Colors.BODY_BACKGROUND.value,
                    border_color=Colors.PRIMARY.value,
                    border_radius='1em',
                    border_width='1px',
                ),
            ),
            rx.link(
                'Inicio',
                href='/',
                display=['none', 'none','flex','flex','flex', 'flex'],
            ),
            rx.link(
                'Sobre Mi',
                href='/about_me',
                display=['none', 'none','flex','flex','flex', 'flex'],
            ),
            rx.tooltip(
                rx.link(
                    'Proyectos',
                    href='/wip',
                    display=['none', 'none','flex','flex','flex', 'flex'],
                ),
                label='Work In Progress'
            ),
            rx.tooltip(
                rx.link(
                    'Blog',
                    href='/wip',
                    display=['none', 'none','flex','flex','flex', 'flex'],
                ),
                label='Work In Progress'
            ),
            rx.tooltip(
                rx.link(
                    'Contacto',
                    href='/wip',
                    display=['none', 'none','flex','flex','flex', 'flex'],
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