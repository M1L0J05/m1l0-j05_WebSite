import reflex as rx
import json

from milo_jos.templates import template
from milo_jos.styles.styles import *
from milo_jos.styles.colors import Colors
from milo_jos.styles.fonts import Fonts, FontWeight


#Variables
with open('assets/texts/about_me.json') as f:
    data = json.load(f)

def quote (quote: str) -> rx.Component:
    return rx.vstack(
        rx.divider(
            border_color=Colors.ACCENT.value
        ),
        rx.spacer(),
        rx.heading(
            f'"{quote}"',
            size='lg',
            as_='i',
            font_family=Fonts.HEADING.value,
        ),
        rx.spacer(),
        rx.divider(
            border_color=Colors.ACCENT.value
        ),
        width='100%'
    )

def mobile_view() -> rx.Component:
    return rx.vstack(
        rx.image(
            src='/img_web_1.png',
        ),
        rx.text(
            data['text_1'],
            text_align='justify',
            color=Colors.CONTENT.value,
        ),

        quote(data['quote_1']),
        
        rx.image(
            src='/img_web_3.png',
        ),
        rx.text(
            data['text_2'],
            text_align='justify',
            color=Colors.CONTENT.value,
        ),

        quote(data['quote_2']),

        rx.image(
            src='/img_web_2.png',
        ),
        rx.text(
            data['text_3'],
            text_align='justify',
            color=Colors.CONTENT.value,
        ),

        display=['flex', 'flex', 'flex', 'none', 'none', 'none'],
        spacing=Size.BIG.value,
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
                src='/img_web_1.png',
                max_width='395px'
            ),
        ),

        rx.spacer(),
        quote(data['quote_1']),
        rx.spacer(),

        rx.hstack(
            rx.image(
                max_height='395px',
                src='/img_web_3.png',
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
        quote(data['quote_2']),
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
                src='/img_web_2.png',
            ),
        ),

        display=['none', 'none','none','flex','flex', 'flex'],
        spacing=Size.BIG.value,
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

