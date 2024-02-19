import reflex as rx

from milo_jos.styles.colors import Colors
from milo_jos.styles.fonts import Fonts, FontWeight


def quote (quote: str='', size='5', *args, **kwargs) -> rx.Component:
    return rx.vstack(
        rx.divider(
            background_color=Colors.ACCENT.value
        ),
        rx.spacer(),
        rx.text(
            quote,
            font_family=Fonts.HEADING.value,
            size=size,
            *args,
            **kwargs,
        ),
        rx.spacer(),
        rx.divider(
            background_color=Colors.ACCENT.value
        ),
        width='100%',
        justify='center',
        align='center',
    )
