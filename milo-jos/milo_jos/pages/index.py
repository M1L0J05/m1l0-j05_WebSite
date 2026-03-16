"""Página principal — smoke test mínimo."""

import reflex as rx


def index() -> rx.Component:
    """Página index mínima para verificar que Reflex arranca."""
    return rx.box(
        rx.heading("M1L0_J05", size="8"),
        rx.text("Smoke test — Reflex 0.8.6 funcionando."),
        padding="2em",
    )
