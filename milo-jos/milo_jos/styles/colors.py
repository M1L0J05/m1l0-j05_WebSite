from enum import Enum


class Colors(Enum):
    BODY_BACKGROUND = "#171F26cc" 
    BACKGROUND = "#0A1637" #-> Black Pearl
    PRIMARY = "#335DB8" # -> Cerlean Blue
    SECONDARY = "#4EA0ED" # -> Picton Blue
    CONTENT = "#DADADE" # -> Mischka
    ACCENT = "#CB91E5" # -> Lavander

class TextColors(Enum):
    DEFAULT = Colors.SECONDARY.value
    #HEADER = "#F1F2F4"
    #FOOTER = "#A3ABB2"

# Color Palette
    #0A1637 -> Black Pearl
    #335DB8 -> Cerlean Blue
    #CB91E5 -> Lavander
    #4EA0ED -> Picton Blue
    #DADADE -> Mischka

# Icons Web ---> https://iconbuddy.app/search