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
	'/custom_style_sheets/normalize.css',
]


# Sizes
class Size(Enum):
	ZERO = '0px !important'
	VERY_SMALL = '0.3em !important'
	SMALL = '0.5em !important'
	MEDIUM = '0.8em !important'
	DEFAULT = '1em !important'
	LARGE = '1.5em !important'
	BIG = '2em !important'
	VERY_BIG = '3em !important'


# Base styles.
BASE_STYLES = {
	'font_family' : Fonts.DEFAULT.value,
	'font_weight' : FontWeight.DEFAULT.value,
	'color' : Colors.PRIMARY.value,
	'background_image' :'circuit-board.svg', 
	rx.Link : {
		'text_decoration' : 'None',
		'_hover' : {
			'text_decoration' : 'None',
			'color' : Colors.CONTENT.value,
		}
	}
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