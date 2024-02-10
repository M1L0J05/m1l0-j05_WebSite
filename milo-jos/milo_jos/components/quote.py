import reflex as rx

from milo_jos.styles.colors import Colors
from milo_jos.styles.fonts import Fonts, FontWeight


def quote (quote: str='') -> rx.Component:
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
