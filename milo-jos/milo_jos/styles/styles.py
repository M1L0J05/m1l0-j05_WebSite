from enum import Enum

import reflex as rx

from milo_jos.styles.fonts import Fonts, FontWeight
from milo_jos.styles.colors import Colors, TextColors

# Constants
MAX_WIDTH = '50em'


# External style sheets
STYLE_SHEETS = [
        "https://fonts.googleapis.com/css2?family=Poppins:wght@100;300;500;700&display=swap",
]


# Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


# Base styles.
BASE_STYLES = {
    'font_family' : Fonts.DEFAULT.value,
    'font_weight' : FontWeight.DEFAULT.value,
    'color' : TextColors.DEFAULT.value,
    'background_color' : Colors.BODY_BACKGROUND.value,
    'background_image' :'circuit-board.svg', 
}