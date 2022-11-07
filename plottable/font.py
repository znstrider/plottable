import colorsys
import math
from typing import Tuple


def contrasting_font_color(
    rgb: Tuple[float],
    light_color: str = "#ffffff",
    dark_color: str = "#000000",
    thresh=186,
) -> str:
    """Automatically chooses a light ("#ffffff") or dark ("#000000") fontcolor based on
    a (background) color.

    Args:
        rgb (Tuple[float]):
            rgb color tuple
        light_color (str, optional)
            the light color to use for dark backgrounds. Defaults to #ffffff
        dark_color (str, optional):
            the dark color to use for light backgrounds. Defaults to #000000
        thresh (int, optional):
            threshold to use. Defaults to 186.

    Returns:
        str: color hex code
    """
    r, g, b = rgb[:3]
    if (r * 0.299 * 256 + g * 0.587 * 256 + b * 0.114 * 256) > thresh:
        return dark_color
    else:
        return light_color


def contrasting_font_color_w3c(
    rgb: Tuple[float],
    light_color: str = "#ffffff",
    dark_color: str = "#000000",
    adjust: float = -0.05,
) -> str:
    """Automatically chooses a light ("#ffffff") or dark ("#000000") fontcolor based on
    a (background) color.

    Args:
        rgb (Tuple[float]): rgb color tuple
        light_color (str, optional)
            the light color to use for dark backgrounds. Defaults to #ffffff
        dark_color (str, optional):
            the dark color to use for light backgrounds. Defaults to #000000
        adjust (float, optional): threshold to use. Defaults to -0.05.

    Returns:
        str: color hex code
    """
    _, l, s = colorsys.rgb_to_hls(*rgb[:3])

    if l > math.sqrt(1.05 * 0.05) + adjust:
        return dark_color
    else:
        return light_color


def contrasting_font_color_(
    rgb: Tuple[float], light_color: str = "#ffffff", dark_color: str = "#000000"
) -> str:
    """Automatically chooses a light ("#ffffff") or dark ("#000000") fontcolor based on
    a (background) color.

    Args:
        rgb (Tuple[float]): rgb color tuple
        light_color (str, optional)
            the light color to use for dark backgrounds. Defaults to #ffffff
        dark_color (str, optional):
            the dark color to use for light backgrounds. Defaults to #000000

    Returns:
        str: color hex code
    """
    _, l, s = colorsys.rgb_to_hls(*rgb[:3])

    if l > math.sqrt(1.05 * 0.05):
        return dark_color
    else:
        return light_color
