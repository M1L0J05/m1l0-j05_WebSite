import reflex as rx

from milo_jos.templates import template
from milo_jos.styles.styles import *
from milo_jos.styles.colors import Colors
from milo_jos.styles.fonts import Fonts, FontWeight


#Variables
texto1 = 'Soy'
texto2 = ' Emilio José'
texto3 = ', entusiasta y apasionado por la tecnología, programación,  diseño web y sobre todo 100% autodidacta. Esta web es un proyecto personal de código libre, una aventura de aprendizaje que comparto contigo. Gracias por visitar mi espacio creativo.'

@template(route='/', title='m1l0_j05 WebSite')
def index() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            rx.avatar(
                src='/images/index/milo_jos.png',
                min_height='512px',
                width='auto',
                border_width='3px',
                border_color=Colors.PRIMARY.value,
                radius='full',
                margin_y=Size.DEFAULT.value
            ),
            rx.spacer(),

            rx.box(
                rx.vstack(
                    rx.text('Bienvenidos', color=Colors.PRIMARY.value),
                    rx.text('a mi', color=Colors.PRIMARY.value),
                    rx.text('WebSite', color=Colors.PRIMARY.value),
                    color=Colors.PRIMARY.value,
                    align='center',
                    display=['flex', 'flex', 'none', 'none', 'none', 'none'],
                ),
                rx.text(
                    'Bienvenidos a mi WebSite', 
                    color=Colors.PRIMARY.value,
                    display=['none', 'none','flex','flex','flex', 'flex'],
                ),

                font_family =  Fonts.HEADING.value,
                font_weight =  FontWeight.BOLD.value,
                color=Colors.PRIMARY.value,
                font_size=Size.VERY_BIG.value,
                margin_bottom=Size.SMALL.value,
                align='center',
                justify='center',
            ),

            rx.divider(
                background_color=Colors.ACCENT.value,
            ),

            rx.vstack(
                rx.text(
                    texto1,
                    rx.text(
                        texto2,
                        as_='span',
                        color=Colors.SECONDARY.value,
                    ),
                    texto3,
                    
                    color=Colors.CONTENT.value,
                    font_size='1.25em',
                    text_align =['center', 'justify'],
                ),
                margin_y=Size.VERY_BIG.value,

            ),
            
            rx.divider(
                background_color=Colors.ACCENT.value
            ),

            width='95%',
            padding=Size.LARGE.value,
            border_radius=Size.SMALL.value,
            min_width=MIN_WIDTH,
            max_width=MAX_WIDTH,
            justify='center',
            align='center',
        ),
    )