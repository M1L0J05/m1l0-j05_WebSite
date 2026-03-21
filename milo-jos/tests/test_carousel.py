"""Tests del estado del carrusel de proyectos.

Verifica el comportamiento de CarouselState: navegación, clampeo
de índices y generación de EventSpec para scroll programático.
"""

import pytest

from milo_jos.states.carousel_state import CarouselState, TOTAL_CARDS


# =============================================================================
# Happy path
# =============================================================================


def test_total_cards_value() -> None:
    """El total de cards debe coincidir con el número de proyectos activos."""
    assert TOTAL_CARDS == 7


def test_set_active_actualiza_indice() -> None:
    """set_active debe actualizar active_index al valor indicado."""
    state = CarouselState()
    state.set_active(3)
    assert state.active_index == 3


def test_scroll_next_incrementa_indice() -> None:
    """scroll_next debe incrementar active_index en 1."""
    state = CarouselState()
    state.active_index = 2
    state.scroll_next()
    assert state.active_index == 3


def test_scroll_prev_decrementa_indice() -> None:
    """scroll_prev debe decrementar active_index en 1."""
    state = CarouselState()
    state.active_index = 4
    state.scroll_prev()
    assert state.active_index == 3


def test_scroll_to_actualiza_indice() -> None:
    """scroll_to debe actualizar active_index al índice destino."""
    state = CarouselState()
    state.scroll_to(5)
    assert state.active_index == 5


# =============================================================================
# Clampeo de índices (casos límite y error esperado)
# =============================================================================


def test_set_active_clampea_indice_negativo() -> None:
    """set_active con índice negativo debe clampear a 0."""
    state = CarouselState()
    state.set_active(-5)
    assert state.active_index == 0


def test_set_active_clampea_indice_mayor_que_total() -> None:
    """set_active con índice mayor al total debe clampear a TOTAL_CARDS - 1."""
    state = CarouselState()
    state.set_active(TOTAL_CARDS + 10)
    assert state.active_index == TOTAL_CARDS - 1


def test_scroll_next_no_supera_ultimo_indice() -> None:
    """scroll_next en el último card no debe sobrepasar TOTAL_CARDS - 1."""
    state = CarouselState()
    state.active_index = TOTAL_CARDS - 1
    state.scroll_next()
    assert state.active_index == TOTAL_CARDS - 1


def test_scroll_prev_no_baja_de_cero() -> None:
    """scroll_prev en el primer card no debe bajar de 0."""
    state = CarouselState()
    state.active_index = 0
    state.scroll_prev()
    assert state.active_index == 0


def test_scroll_to_clampea_indice_fuera_de_rango() -> None:
    """scroll_to con índice fuera de rango debe clampear al límite más cercano."""
    state = CarouselState()
    state.scroll_to(TOTAL_CARDS + 99)
    assert state.active_index == TOTAL_CARDS - 1
