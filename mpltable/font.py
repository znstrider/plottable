import colorsys
import math
from typing import Tuple


def contrasting_font_color(rgb: Tuple[float], thresh=186) -> str:
    """Automatically chooses a light ("#ffffff") or dark ("#000000") fontcolor based on
    a (background) color.

    Args:
        rgb (Tuple[float]): rgb color tuple
        thresh (int, optional): _description_. Defaults to 186.

    Returns:
        str: _description_
    """
    r, g, b = rgb[:3]
    if (r * 0.299 * 256 + g * 0.587 * 256 + b * 0.114 * 256) > thresh:
        return "#000000"
    else:
        return "#ffffff"


def contrasting_font_color_w3c(rgb: Tuple[float], adjust: float = -0.05) -> str:
    """Automatically chooses a light ("#ffffff") or dark ("#000000") fontcolor based on
    a (background) color.

    Args:
        rgb (Tuple[float]): rgb color tuple
        adjust (float, optional): _description_. Defaults to -0.05.

    Returns:
        str: color hex code
    """
    _, l, s = colorsys.rgb_to_hls(*rgb[:3])

    if l > math.sqrt(1.05 * 0.05) + adjust:
        return "#000000"
    else:
        return "#ffffff"


def contrasting_font_color_(rgb: Tuple[float]) -> str:
    """Automatically chooses a light ("#ffffff") or dark ("#000000") fontcolor based on
    a (background) color.

    Args:
        rgb (Tuple[float]): rgb color tuple

    Returns:
        str: color hex code
    """
    _, l, s = colorsys.rgb_to_hls(*rgb[:3])

    if l > math.sqrt(1.05 * 0.05):
        return "#000000"
    else:
        return "#ffffff"
