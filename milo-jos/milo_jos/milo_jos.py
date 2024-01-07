"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

from milo_jos.styles import styles
from milo_jos.pages import *

class State(rx.State):
    """The app state."""

    pass


# Add state and page to the app.
app = rx.App(
    stylesheets=styles.STYLE_SHEETS,
    style=styles.BASE_STYLES,
)

app.compile()
