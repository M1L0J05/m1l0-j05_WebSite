from enum import Enum

import reflex as rx

from milo_jos.styles.fonts import Fonts, FontWeight
from milo_jos.styles.colors import Colors

# Constants
MIN_WIDTH = '15em' # 240px
MID_WIDTH = '40em' # 720px
MAX_WIDTH = '75em' # 1200px 


# External style sheets
STYLE_SHEETS = [
	'https://fonts.googleapis.com/css2?family=Poppins:wght@100;300;500;700&display=swap',
	'https://fonts.googleapis.com/css2?family=Comfortaa:wght@100;300;500;700&display=swap',
	'https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css',
]


# Sizes
class Size(Enum):
	ZERO = '0px'
	MICRO_SMALL = '0.25em'
	VERY_SMALL = '0.5em'
	SMALL = '0.75em'
	DEFAULT = '1em'
	MEDIUM = '1.5em'
	LARGE = '2em'
	BIG = '2.5em'
	VERY_BIG = '3em'
	EXTRA_BIG = '4em'

class Spacing(Enum):
	ZERO = '0'
	MICRO_SMALL = '1'
	VERY_SMALL = "2"
	SMALL = '3'
	DEFAULT = '4' #16PX / 1em
	MEDIUM = '5'
	LARGE = '6'
	BIG = '7'
	VERY_BIG ='8'
	EXTRA_BIG = '9'

# Base styles.
BASE_STYLES = {
	'font_family' : Fonts.DEFAULT.value,
	'font_weight' : FontWeight.DEFAULT.value,
	'color' : Colors.PRIMARY.value,
	'background_color' : 'black',
	'background_image' : "url(/images/root/circuit-board.svg)", 
	
	rx.link : {
		'text_decoration' : 'None',
		'_hover' : {
			'text_decoration' : 'None',
			'color' : Colors.CONTENT.value,
		}
	},

	rx.text : {
		'color' : Colors.CONTENT.value,
		'text_align' : 'justify',
	}
}

CUSTOM_BOX_STYLES = {
	'color' : Colors.ACCENT.value,
	'border' : f'1px  solid {Colors.PRIMARY.value}',
	'border_radius' : Size.SMALL.value,
	'_hover' : {
		'color': Colors.CONTENT.value,
		'border' : f'0.1em solid {Colors.SECONDARY.value}',
		'cursor' : 'pointer',
	},
}