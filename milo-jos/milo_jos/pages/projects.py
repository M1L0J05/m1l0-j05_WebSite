import json
from typing import Dict, Any, Tuple, List
import reflex as rx


from milo_jos.components import quote
from milo_jos.templates import template
from milo_jos.styles.styles import *
from milo_jos.styles.colors import Colors

with open('assets/data/projects.json') as f:
    projects_data = json.load(f)

"""
def projects_items() -> rx.Component:
    return rx.responsive_grid(
        *[
            rx.card(
                rx.vstack(
                    rx.image(
                        src=projects_data[key]['imagen'],
                        #padding=Size.DEFAULT.value,
                        border_radius=Size.SMALL.value,
                        box_shadow='lg',
                        border=f'1px solid {Colors.SECONDARY.value}',
                        max_width='90%',
                        margin_bottom=Size.DEFAULT.value,
                    ),
                    rx.spacer(),
                    rx.vstack(
                        rx.text(
                            'Tecnologías',
                            color=Colors.SECONDARY.value,
                            font_size=Size.LARGE.value,
                        ),
                        #rx.responsive_grid(
                        #    *[
                        #        rx.text(
                        #            class_name=f'devicon-{tecnologia.lower()}-plain',
                        #            font_size=Size.LARGE.value,
                        #            padding=Size.VERY_SMALL.value,
                        #            text_color=Colors.ACCENT.value,
                        #        )
                        #        for tecnologia in projects_data[key]['tecnologias']
                        #    ],
                        #    columns=[7, 7, 9],
                        #), 
                        #padding=Size.VERY_SMALL.value,
                    ),
                    rx.spacer(),
                    rx.text(
                        'Descripción',
                        color=Colors.SECONDARY.value,
                        font_size=Size.LARGE.value,
                    ),
                    rx.text(
                        projects_data[key]['descripcion'],
                        text_align='justify',
                    ),
                ),
                header = quote(
                    f'{projects_data[key]["nombre"]}',
                    size='xl',
                    padding=Size.SMALL.value,
                    text_align='center',
                    color=Colors.PRIMARY.value,
                ),
                footer=rx.heading(
                    projects_data[key]['fecha_fin'],
                    size='sm',
                    font_family=Fonts.HEADING.value,
                    padding=Size.SMALL.value,
                    text_align='center'
                ),
                box_shadow='0px 0px 35px -15px rgba(148,12,227,0.5)',
            )
            for key, value  in projects_data.items()
        ],

        columns=[1],
        spacing=Size.DEFAULT.value,
        margin_y=Size.VERY_BIG.value,
        padding=Size.SMALL.value,
        width='100%,'
    )

"""

@template(route='/projects', title='m1l0_j05 WebSite')
def projects() -> rx.Component:
    return rx.fragment(
        rx.vstack(
            #rx.image(
            #    src='/images/banner_project.svg',
            #    min_width=Size.EXTRA_BIG.value,
            #),
            #quote(
            #    'Proyectos',
            #    size='2xl',
            #),
            rx.spacer(),
            #projects_items(),
            rx.spacer(),

            width='95%',
            border_radius=Size.SMALL.value,
            min_width=MIN_WIDTH,
            max_width=MAX_WIDTH,
        ),
    )

