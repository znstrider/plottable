import pytest

from plottable.font import (
    contrasting_font_color,
    contrasting_font_color_,
    contrasting_font_color_w3c,
)

font_color_fns = (
    contrasting_font_color,
    contrasting_font_color_,
    contrasting_font_color_w3c,
)


@pytest.mark.parametrize("fn", font_color_fns)
def test_font_color_fns_black_on_white_bg(fn):
    white = (1, 1, 1)
    assert fn(white) == "#000000"


@pytest.mark.parametrize("fn", font_color_fns)
def test_font_color_fns_white_on_black_bg(fn):
    black = (0, 0, 0)
    assert fn(black) == "#ffffff"


@pytest.mark.parametrize("fn", font_color_fns)
def test_font_color_fns_custom_dark_on_white_bg(fn):
    white = (1, 1, 1)
    custom = "#252526"
    assert fn(white, dark_color=custom) == custom


@pytest.mark.parametrize("fn", font_color_fns)
def test_font_color_fns_custom_light_on_black_bg(fn):
    black = (0, 0, 0)
    custom = "#f0f0f0"
    assert fn(black, light_color=custom) == custom
