import reflex as rx
import json

from milo_jos.templates import template
from milo_jos.styles.styles import *
from milo_jos.styles.colors import Colors
from milo_jos.styles.fonts import Fonts, FontWeight
from milo_jos.components import quote


#Variables
with open('assets/data/about_me.json') as f:
    data = json.load(f)


def mobile_view() -> rx.Component:
    return rx.vstack(
        rx.image(
            src='/images/img_web_1.png',
        ),
        rx.text(
            data['text_1'],
            text_align='justify',
            color=Colors.CONTENT.value,
        ),

        quote(
            f'"{data["quote_1"]}"', 
            as_='em',
            text_align='center',
            size='6',
            weight='bold',
        ),
        
        rx.image(
            src='/images/img_web_3.png',
        ),
        rx.text(
            data['text_2'],
            text_align='justify',
            color=Colors.CONTENT.value,
        ),

        quote(
            f'"{data["quote_2"]}"', 
            as_='em',
            text_align='center',
            size='6',
            weight='bold',
        ),

        rx.image(
            src='/images/img_web_2.png',
        ),
        rx.text(
            data['text_3'],
            text_align='justify',
            color=Colors.CONTENT.value,
        ),

        display=['flex', 'flex', 'flex', 'none', 'none', 'none'],
        spacing='5',
        padding=Size.SMALL.value,
    )


def normal_view() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text(
                data['text_1'],
                text_align='justify',
                color=Colors.CONTENT.value,
                margin='auto',
                padding=Size.DEFAULT.value,
            ),
            rx.image(
                src='/images/img_web_1.png',
                max_width='395px'
            ),
        ),

        rx.spacer(),
        quote(
            f'"{data["quote_1"]}"', 
            as_='em',
            text_align='center',
            size='6',
            weight='bold',
        ),
        rx.spacer(),

        rx.hstack(
            rx.image(
                max_height='395px',
                src='/images/img_web_3.png',
            ),
            rx.text(
                data['text_2'],
                text_align='justify',
                color=Colors.CONTENT.value,
                margin='auto',
                padding=Size.DEFAULT.value,
            ),

        ),

        rx.spacer(),
        quote(
            f'"{data["quote_2"]}"', 
            as_='em',
            text_align='center',
            size='6',
            weight='bold',
        ),
        rx.spacer(),

        rx.hstack(
            rx.text(
                data['text_3'],
                text_align='justify',
                color=Colors.CONTENT.value,
                margin='auto',
                padding=Size.DEFAULT.value,
            ),
            rx.image(
                max_height='395px',
                src='/images/img_web_2.png',
            ),
        ),

        display=['none', 'none','none','flex','flex', 'flex'],
        spacing='3',
        justify='center',
        align='center',
    )


@template(route='/about_me', title='m1l0_j05 WebSite')
def about_me() -> rx.Component:
    return rx.vstack(
        mobile_view(),
        normal_view(),

        width='100%',
        padding=Size.SMALL.value,
        min_width=MIN_WIDTH,
        max_width=MAX_WIDTH,
        margin_y=Size.VERY_BIG.value,
    )

