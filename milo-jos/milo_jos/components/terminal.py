"""Terminal — Bloque de terminal para la hero section.

Simula una ventana de terminal con prompt $ en verde,
comandos en blanco y output en gris. Efecto typewriter CSS
con delay incremental por cada línea de comando.

Especificaciones: docs/architecture.md > Componentes UI > Terminal
"""

import reflex as rx

from milo_jos.styles import Color, FontFamily, FontSize, FontWeight

# Duración base de la animación typewriter por línea de comando (segundos).
_TYPEWRITER_DURATION: float = 0.7
# Delay inicial antes de que comience la primera animación (segundos).
_TYPEWRITER_INITIAL_DELAY: float = 0.2


def _terminal_line(
    prompt: str = "$",
    command: str = "",
    output: str = "",
    *,
    is_output_only: bool = False,
    delay: float = 0,
) -> rx.Component:
    """Línea individual del terminal con efecto typewriter opcional.

    Args:
        prompt: Carácter de prompt (default '$').
        command: Comando a mostrar.
        output: Salida del comando.
        is_output_only: Si True, solo muestra output sin prompt.
        delay: Retardo en segundos antes de iniciar la animación
               typewriter. Solo aplica a líneas de comando.

    Returns:
        Componente con una línea de terminal.
    """
    if is_output_only:
        # Líneas de output: aparecen tras el comando con fade-in
        output_delay = delay
        return rx.text(
            output,
            font_family=FontFamily.MONO,
            font_size=FontSize.SMALL,
            color=Color.TEXT_SECONDARY,
            line_height="1.8",
            white_space="pre-wrap",
            opacity="0",
            animation=f"reveal 0.2s ease-out {output_delay}s both",
        )

    # Líneas de comando: efecto typewriter sin cursor parpadeante
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
        white_space="nowrap",
        overflow="hidden",
        max_width="100%",
        animation=f"typewriter {_TYPEWRITER_DURATION}s steps(30, end) {delay}s both",
    )


def terminal_block(
    lines: list[dict],
    *,
    title: str = "terminal",
) -> rx.Component:
    """Bloque de terminal completo con barra de título y typewriter.

    Calcula delays incrementales para cada línea de comando,
    de forma que se animen secuencialmente como si se estuviera
    escribiendo en una terminal real.

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

    # Cuerpo del terminal con delays incrementales
    body_lines: list[rx.Component] = []
    current_delay: float = _TYPEWRITER_INITIAL_DELAY

    for line in lines:
        if "command" in line:
            body_lines.append(
                _terminal_line(
                    prompt=line.get("prompt", "$"),
                    command=line["command"],
                    delay=current_delay,
                )
            )
            # Avanzar el delay: duración de escritura + pequeña pausa
            current_delay += _TYPEWRITER_DURATION + 0.15
        if "output" in line:
            body_lines.append(
                _terminal_line(
                    output=line["output"],
                    is_output_only=True,
                    delay=current_delay,
                )
            )
            # Pequeña pausa tras el output antes del siguiente comando
            current_delay += 0.2

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
        max_width=["100%", "100%", "600px"],
        overflow="hidden",
    )
