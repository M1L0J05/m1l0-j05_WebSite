"""Paquete de componentes UI — milo-jos.es v2.0.

Re-exporta todos los componentes reutilizables:

    from milo_jos.components import navbar, footer, badge, primary_button
"""

from .badge import badge, status_badge
from .button import primary_button, secondary_button
from .card import coming_soon_card, project_card
from .footer import footer
from .navbar import navbar
from .terminal import terminal_block
from .timeline import timeline, timeline_item

__all__: list[str] = [
    "badge",
    "coming_soon_card",
    "footer",
    "navbar",
    "primary_button",
    "project_card",
    "secondary_button",
    "status_badge",
    "terminal_block",
    "timeline",
    "timeline_item",
]
