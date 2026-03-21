"""Animaciones CSS — Keyframes para milo-jos.es.

Define las animaciones reutilizables del sistema de diseño.
Se inyectan como CSS global vía rx.html.style en el template.

Reglas:
- Solo propiedades GPU: transform, opacity
- prefers-reduced-motion: desactivar todas
- Máximo 3 animaciones simultáneas
"""

# --- Keyframes como strings CSS ---

KEYFRAME_BLINK: str = """
@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
}
"""

KEYFRAME_TYPEWRITER: str = """
@keyframes typewriter {
    from { width: 0; }
    to { width: 100%; }
}
"""

KEYFRAME_GLOW_PULSE: str = """
@keyframes glow-pulse {
    0%, 100% { box-shadow: 0 0 8px rgba(0, 180, 216, 0.4); }
    50% { box-shadow: 0 0 20px rgba(0, 180, 216, 0.8); }
}
"""

KEYFRAME_FADE_IN_UP: str = """
@keyframes fade-in-up {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
"""

KEYFRAME_BOUNCE: str = """
@keyframes bounce {
    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-8px); }
    60% { transform: translateY(-4px); }
}
"""

KEYFRAME_GRADIENT_SHIFT: str = """
@keyframes gradient-shift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
"""

KEYFRAME_REVEAL: str = """
@keyframes reveal {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
"""
"""Keyframe de revelación para secciones al hacer scroll."""

# Fallback de glassmorphism para navegadores sin soporte de backdrop-filter.
# Define variables CSS que cambian a fondos opacos cuando no hay soporte,
# evitando que el contenido se vea a través sin desenfoque.
GLASSMORPHISM_FALLBACK: str = """
:root {
    --glass-bg-card: rgba(22, 27, 34, 0.6);
    --glass-bg-navbar: rgba(22, 27, 34, 0.6);
    --glass-blur-card: blur(12px);
    --glass-blur-navbar: blur(16px);
}
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
    :root {
        --glass-bg-card: rgba(22, 27, 34, 0.95);
        --glass-bg-navbar: rgba(22, 27, 34, 0.95);
    }
}
"""

# Regla de accesibilidad: desactivar animaciones si el usuario lo prefiere.
# Incluye scroll-behavior para evitar scroll suave no deseado.
REDUCED_MOTION: str = """
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
    html {
        scroll-behavior: auto !important;
    }
}
"""

# CSS para ocultar la scrollbar nativa del carrusel de proyectos.
# Usa class_name="carousel-scroll-container" en el contenedor flex.
CAROUSEL_SCROLLBAR_HIDE: str = """
.carousel-scroll-container::-webkit-scrollbar {
    display: none;
}
.carousel-scroll-container {
    -ms-overflow-style: none;
    scrollbar-width: none;
}
"""

# --- Shortcuts para aplicar en props de estilo ---

class Animation:
    """Valores CSS listos para usar en la prop `animation`."""

    CURSOR_BLINK: str = "blink 1s step-end infinite"
    """Cursor █ del wordmark."""

    TYPEWRITER: str = "typewriter 2s steps(40, end) forwards"
    """Efecto máquina de escribir en terminal."""

    GLOW_PULSE: str = "glow-pulse 2s ease-in-out infinite"
    """Glow pulsante en dot activo del timeline."""

    FADE_IN_UP: str = "fade-in-up 0.5s ease-out forwards"
    """Reveal al hacer scroll (secciones)."""

    SCROLL_BOUNCE: str = "bounce 2s ease-in-out infinite"
    """Indicador de scroll en hero."""

    GRADIENT: str = "gradient-shift 8s ease infinite"
    """Gradiente animado del hero background."""

    REVEAL: str = "reveal 0.6s ease-out both"
    """Revelación suave de secciones al cargar."""


def get_all_keyframes() -> str:
    """Devuelve todos los keyframes concatenados para inyectar en CSS global.

    Returns:
        String con todas las reglas @keyframes y @media.
    """
    return "\n".join([
        KEYFRAME_BLINK,
        KEYFRAME_TYPEWRITER,
        KEYFRAME_GLOW_PULSE,
        KEYFRAME_FADE_IN_UP,
        KEYFRAME_BOUNCE,
        KEYFRAME_GRADIENT_SHIFT,
        KEYFRAME_REVEAL,
        GLASSMORPHISM_FALLBACK,
        REDUCED_MOTION,
        CAROUSEL_SCROLLBAR_HIDE,
    ])
