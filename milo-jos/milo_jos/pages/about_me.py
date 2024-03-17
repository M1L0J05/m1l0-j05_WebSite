import reflex as rx
import json

from milo_jos.templates import template
from milo_jos.styles.styles import *
from milo_jos.styles.colors import Colors
from milo_jos.styles.fonts import Fonts, FontWeight
from milo_jos.components import quote

data = {
    "quote_1" : "Exploré calles y forje caminos que marcarían mi trayectoria hasta el día de hoy.",
    "quote_2" : "Autodidacta en constante evolución, navengando entre recursos y agradecido por cada paso del viaje.",
    "text_1" : "Nací en Linares (Jaén) un soleado día del mes de marzo de 1981. Pasé mi infancia y adolescencia explorando las calles de esa pequeña pero gran ciudad hasta los 18 años. Después, comencé mi viaje por la vida y el trabajo. Me aventuré primero en Cáceres, luego en Córdoba, donde pasé 6 años, durante los cuales estuve 6 meses en Rajlovac (Sarajevo). Terminada esa etapa, regresé a Jaén por un tiempo, donde estuve en Baeza y Bailén. Más tarde, volví a marchar y finalmente encontré mi hogar en el vibrante Bilbao, en Bizkaia, donde actualmente resido.",
    "text_2" : "Por diversos motivos y experiencias de vida, solo completé los estudios obligatorios. Me lancé al mundo laboral, dedicándome a servir y proteger dentro y fuera de mi país. Este camino me llevó a seguir sirviendo y protegiendo, haciendo del honor mi divisa. Me especialicé en la obtención y elaboración de información, uniéndome a un equipo excepcional de personas abnegadas y luchadoras. En esta especialidad y conforme avanzaban las tecnologías tuve la suerte de empezar a formar parte de un equipo pequeño en el que nuestra labor se centra en el mantenimiento informático y sistemas, OSINT e I+D+i. Aquí creamos, adaptamos, implementamos y mantenemos diversas herramientas que facilitan las labores del trabajo diario. Es un ambiente dinámico donde la colaboración, la creatividad y la amistad son fundamentales.",
    "text_3" : "A lo largo de mi trayectoria, he sido 100% autodidacta. He consumido una amplia variedad de recursos, incluyendo videos, cursos en línea y todo tipo de conocimientos al alcance de mi mano. Esto me ha llevado a adquirir experiencia avanzada en lenguajes de programción, especialmente Python, diseño web y en menor medida en tecnologías de sistemas y microservicios. En la sección de proyectos, podrás ver todo lo que he logrado crear, comenzando desde cero, sin experiencia y conocimientos teóricos previos. Por último, quiero expresar mi más sincero agradecimiento por tomarte el tiempo de conocer mi pequeña historia."
}

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

