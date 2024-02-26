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
            src='/images/about_me/img_web_1.webp',
        ),
        rx.text(
            data['text_1'],
        ),

        quote(
            f'"{data["quote_1"]}"', 
            as_='em',
            text_align='center',
            size=Spacing.BIG.value,
            weight='bold',
        ),
        
        rx.image(
            src='/images/about_me/img_web_3.webp',
        ),

        rx.text(
            data['text_2'],
        ),

        quote(
            f'"{data["quote_2"]}"', 
            as_='em',
            text_align='center',
            size=Spacing.BIG.value,
            weight='bold',
        ),

        rx.image(
            src='/images/about_me/img_web_2.webp',
        ),

        rx.text(
            data['text_3'],
        ),

        display=['flex', 'flex', 'flex', 'none', 'none', 'none'],
        spacing=Spacing.MEDIUM.value,
        padding=Size.DEFAULT.value,
        align='center',
        justify='center'
    )


def normal_view() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text(
                data['text_1'],
                margin='auto',
                padding=Size.DEFAULT.value,
            ),
            rx.image(
                src='/images/about_me/img_web_1.webp',
                max_width='395px'
            ),
        ),

        rx.spacer(),

        quote(
            f'"{data["quote_1"]}"', 
            as_='em',
            text_align='center',
            size=Spacing.VERY_BIG.value,
            weight='bold',
        ),
        rx.spacer(),

        rx.hstack(
            rx.image(
                max_height='395px',
                src='/images/about_me/img_web_3.webp',
            ),
            rx.text(
                data['text_2'],
                margin='auto',
                padding=Size.DEFAULT.value,
            ),
        ),

        rx.spacer(),

        quote(
            f'"{data["quote_2"]}"', 
            as_='em',
            text_align='center',
            size=Spacing.VERY_BIG.value,
            weight='bold',
        ),
        
        rx.spacer(),

        rx.hstack(
            rx.text(
                data['text_3'],
                margin='auto',
                padding=Size.DEFAULT.value,
            ),
            rx.image(
                max_height='395px',
                src='/images/about_me/img_web_2.webp',
            ),
        ),

        display=['none', 'none','none','flex','flex', 'flex'],
        spacing=Spacing.MEDIUM.value,
        justify='center',
        align='center',
        font_size='1.25em',
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

