import json
import reflex as rx


from milo_jos.components import quote
from milo_jos.templates import template
from milo_jos.styles.styles import *
from milo_jos.styles.colors import Colors


# Abrimos el archivo JSON con los datos de los proyectos
with open('assets/data/projects.json') as f:
    json_data = json.load(f)  # Cargamos los datos del archivo JSON

class Proyectos(rx.State):
    proyectos:  list[dict] = json_data['proyectos']

    #def get_data(self):
    #    with open('assets/data/projects.json') as f:
    #        json_data = json.load(f)
    #    print(json_data['proyectos'])
    #    self.proyectos = json_data['proyectos']


    def card_proyecto(self, proyecto: dict):
        return rx.card(
            rx.inset(
                rx.image(
                    src=proyecto['imagen'],
                    width='100%',
                    margin='auto'
                ),
                side="top",
                pb="current",
            ),
            quote(
                proyecto['nombre'],
                text_align='center',
                font_weight=FontWeight.BOLD.value,
                size=Spacing.LARGE.value,
            ),
            rx.text(
                '- Resumen -',
                color=Colors.SECONDARY.value,
                text_align='center',
                font_size=Size.MEDIUM.value,
                margin_top=Size.DEFAULT.value,
                margin_bottom=Size.MICRO_SMALL.value,
            ),
            rx.text(
                proyecto['resumen'],
            ),
            rx.text(
                '- Tecnologías -',
                color=Colors.SECONDARY.value,
                text_align='center',
                font_size=Size.MEDIUM.value,
                margin_y=Size.MICRO_SMALL.value,
            ),
            rx.flex(
                *[
                    rx.text(
                        class_name=f'devicon-{tech.lower()}-plain',
                        font_size=Size.MEDIUM.value,
                    )
                    for tech in proyecto['tecnologias']
                ],
                wrap='wrap',
                spacing=Spacing.SMALL.value,
                justify='center',
                align='center', 
            ),
            rx.text(
                '- Inicio & Fin -',
                color=Colors.SECONDARY.value,
                text_align='center',
                font_size=Size.MEDIUM.value,
                margin_y=Size.MICRO_SMALL.value,
            ),
            rx.vstack(
                rx.text(
                    proyecto['fecha_inicio'], 
                    text_align='center',
                ),
                rx.text(
                    proyecto['fecha_fin'].upper(), 
                    color=Colors.ACCENT.value,
                    text_align='center',
                ),
                align='center',
                justify='center'
            ),

            max_width=MID_WIDTH,
            background_color='transparent',
            size=Spacing.DEFAULT.value,
            width=['90vw','90vw','45vw','45vw','33vw',],
        )
    
    def render_proyecto(self ):
        return rx.flex(
            *[
                self.card_proyecto(
                    proyecto
                )
                for proyecto in self.proyectos
            ],
            spacing=Spacing.SMALL.value,
            justify='center',
            flex_wrap='wrap',
            margin='auto',
        )


@template(route='/projects', title='m1l0_j05 WebSite', )
def projects( ) -> rx.Component:
    proyectos = Proyectos()
    return rx.fragment(
        rx.vstack(
            rx.spacer(),
            proyectos.render_proyecto(),
            width='95%',
            min_width=MIN_WIDTH,
            margin_top=Size.BIG.value,
        ),
    )