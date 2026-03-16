"""Terminal — Bloque de terminal para la hero section.

Simula una ventana de terminal con prompt $ en verde,
comandos en blanco y output en gris. Efecto typewriter CSS.

Especificaciones: docs/architecture.md > Componentes UI > Terminal
"""

import reflex as rx

from milo_jos.styles import Color, FontFamily, FontSize, FontWeight


def _terminal_line(
    prompt: str = "$",
    command: str = "",
    output: str = "",
    *,
    is_output_only: bool = False,
) -> rx.Component:
    """Línea individual del terminal.

    Args:
        prompt: Carácter de prompt (default '$').
        command: Comando a mostrar.
        output: Salida del comando.
        is_output_only: Si True, solo muestra output sin prompt.

    Returns:
        Componente con una línea de terminal.
    """
    if is_output_only:
        return rx.text(
            output,
            font_family=FontFamily.MONO,
            font_size=FontSize.SMALL,
            color=Color.TEXT_SECONDARY,
            line_height="1.8",
            white_space="pre-wrap",
        )

    children = [
        rx.text.span(
            f"{prompt} ",
            color=Color.ACCENT_GREEN,
            font_weight=FontWeight.BOLD,
        ),
        rx.text.span(
            command,
            color=Color.TEXT_PRIMARY,
        ),
    ]

    return rx.text(
        *children,
        font_family=FontFamily.MONO,
        font_size=FontSize.SMALL,
        line_height="1.8",
        white_space="pre-wrap",
    )


def terminal_block(
    lines: list[dict],
    *,
    title: str = "terminal",
) -> rx.Component:
    """Bloque de terminal completo con barra de título.

    Args:
        lines: Lista de líneas. Cada dict puede tener:
            - {"command": "whoami"} → $ whoami
            - {"output": "M1L0_J05"} → texto gris sin prompt
            - {"command": "cat stack.txt", "prompt": ">"} → > cat stack.txt
        title: Título de la ventana del terminal.

    Returns:
        Componente que simula una ventana de terminal.
    """
    # Barra de título con dots decorativos
    title_bar = rx.hstack(
        # Dots estilo macOS
        rx.hstack(
            rx.box(
                width="12px",
                height="12px",
                border_radius="50%",
                background_color="#FF5F56",
            ),
            rx.box(
                width="12px",
                height="12px",
                border_radius="50%",
                background_color="#FFBD2E",
            ),
            rx.box(
                width="12px",
                height="12px",
                border_radius="50%",
                background_color="#27C93F",
            ),
            spacing="2",
        ),
        rx.spacer(),
        rx.text(
            title,
            font_family=FontFamily.MONO,
            font_size=FontSize.MICRO,
            color=Color.TEXT_SECONDARY,
        ),
        rx.spacer(),
        # Espacio equivalente para centrar el título
        rx.box(width="52px"),
        width="100%",
        padding_x="1rem",
        padding_y="0.75rem",
        border_bottom=f"1px solid {Color.BORDER}",
        align_items="center",
    )

    # Cuerpo del terminal
    body_lines: list[rx.Component] = []
    for line in lines:
        if "command" in line:
            body_lines.append(
                _terminal_line(
                    prompt=line.get("prompt", "$"),
                    command=line["command"],
                )
            )
        if "output" in line:
            body_lines.append(
                _terminal_line(output=line["output"], is_output_only=True)
            )

    body = rx.vstack(
        *body_lines,
        spacing="0",
        padding="1rem",
        width="100%",
        align_items="flex-start",
    )

    return rx.box(
        title_bar,
        body,
        background_color=Color.BG_BASE,
        border=f"1px solid {Color.BORDER}",
        border_radius="8px",
        width="100%",
        max_width="600px",
        overflow="hidden",
    )
