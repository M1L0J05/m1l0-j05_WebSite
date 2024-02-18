import reflex as rx

from milo_jos.styles.colors import Colors
from milo_jos.styles.fonts import Fonts, FontWeight


def quote (quote: str='', size='lg', *args, **kwargs) -> rx.Component:
    return rx.vstack(
        rx.divider(
            border_color=Colors.ACCENT.value
        ),
        rx.spacer(),
        rx.heading(
            quote,
            #size=size,
            font_family=Fonts.HEADING.value,
            *args,
            **kwargs,
        ),
        rx.spacer(),
        rx.divider(
            border_color=Colors.ACCENT.value
        ),
        width='100%'
    )
