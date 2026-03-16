from rxconfig import config

import reflex as rx

from milo_jos.styles import styles
from milo_jos.pages import *


# Add state and page to the app.
app = rx.App(
    stylesheets=styles.STYLE_SHEETS,
    style=styles.BASE_STYLES,
)
