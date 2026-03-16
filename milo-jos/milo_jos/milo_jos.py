"""Punto de entrada de la aplicación Reflex."""

import reflex as rx

from milo_jos.pages.index import index

app = rx.App()
app.add_page(index, route="/", title="M1L0_J05")
