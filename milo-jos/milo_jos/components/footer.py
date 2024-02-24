import reflex as rx

from milo_jos.styles.styles import Size, Colors, Spacing
from milo_jos.styles.fonts import FontWeight
from datetime import datetime


def footer() -> rx.Component:
    year = datetime.now().year
    years_copy = f'\u00A9 2023-{year} '
    return rx.vstack(
        rx.link(
            rx.text(
                class_name='devicon-github-original',
                font_size=Size.BIG.value,
                color=Colors.PRIMARY.value,
            ),
            href='https://github.com/M1L0J05/m1l0-j05_WebSite',
            is_external=True,
            padding=Size.MICRO_SMALL.value,
            color=Colors.PRIMARY.value,
        ), 
        
        rx.text(
            years_copy,
            rx.text(
                'Creado por m1l0_j05 ', 
                color=Colors.ACCENT.value,
                as_='span'   
            ),
            'V1.'
        ),

        rx.text(
            'Explora, descubre y crea tu propio camino.',
        ),

        rx.text(
            'I',
            rx.text(
                ' LoVe ',
                color='red',
                font_weight=FontWeight.BOLD.value,
                as_='span'
            ),
            'Linares!',
            color=Colors.SECONDARY.value, 
        ),

        spacing=Spacing.MICRO_SMALL.value,
        color=Colors.CONTENT.value,
        font_size=Size.SMALL.value,
        padding=Size.DEFAULT.value,
        align='center',
        justify='center',
        margin_x='auto',
        margin_y=Size.DEFAULT.value,

    )