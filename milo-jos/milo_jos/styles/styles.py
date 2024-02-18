from enum import Enum

import reflex as rx

from milo_jos.styles.fonts import Fonts, FontWeight
from milo_jos.styles.colors import Colors

# Constants
MIN_WIDTH = '15em !important' # 240px
MAX_WIDTH = '75em !important' # 1200px 


# External style sheets
STYLE_SHEETS = [
	'https://fonts.googleapis.com/css2?family=Poppins:wght@100;300;500;700&display=swap',
	'https://fonts.googleapis.com/css2?family=Comfortaa:wght@100;300;500;700&display=swap',
	'https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css',
]


# Sizes
class Size(Enum):
	ZERO = '0px !important'
	MICRO = '0.1em !important'
	VERY_SMALL = '0.3em !important'
	SMALL = '0.5em !important'
	MEDIUM = '0.8em !important'
	DEFAULT = '1em !important'
	LARGE = '1.5em !important'
	BIG = '2em !important'
	MEDIUM_BIG = '2.5em !important'
	VERY_BIG = '3em !important'
	EXTRA_BIG = '4em !important'


# Base styles.
BASE_STYLES = {
	'font_family' : Fonts.DEFAULT.value,
	'font_weight' : FontWeight.DEFAULT.value,
	'color' : Colors.PRIMARY.value,
	'background_color' : 'black',
	'background_image' : "url(/images/circuit-board.svg)", 
	
	rx.link : {
		'text_decoration' : 'None',
		'_hover' : {
			'text_decoration' : 'None',
			'color' : Colors.CONTENT.value,
		}
	},


	rx.card : {
		#'width' : '100%,',
		#'variant' : 'outline',
		'padding' : Size.DEFAULT.value,
		'background_color' : Colors.BODY_BACKGROUND.value,
		'color' : Colors.CONTENT.value,
		'border' : f'1px solid {Colors.BACKGROUND.value}',
	},
}


CUSTOM_BOX_STYLES = {
	'color' : Colors.ACCENT.value,
	'border' : '1px  solid #335DB8',
	'border_radius' : Size.SMALL.value,
	'_hover' : {
		'color': Colors.CONTENT.value,
		'border' : '0.1em solid #4EA0ED',
		'cursor' : 'pointer',
	},
}