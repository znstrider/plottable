from __future__ import annotations

from typing import Callable

import matplotlib
import pandas as pd
from matplotlib.colors import TwoSlopeNorm


def normed_cmap(
    s: pd.Series, cmap: matplotlib.colors.LinearSegmentedColormap, num_stds: float = 2.5
) -> Callable:
    """Returns a normalized colormap function that takes a float as an argument and
    returns an rgba value.

    Args:
        s (pd.Series):
            a series of numeric values
        cmap (matplotlib.colors.LinearSegmentedColormap):
            matplotlib Colormap
        num_stds (float, optional):
            vmin and vmax are set to the median ± num_stds.
            Defaults to 2.5.

    Returns:
        Callable: Callable that takes a float as an argument and returns an rgba value.
    """
    _median = s.median()
    _std = s.std()

    vmin = _median - num_stds * _std
    vmax = _median + num_stds * _std

    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
    m = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)

    return m.to_rgba


def centered_cmap(
    s: pd.Series,
    cmap: matplotlib.colors.LinearSegmentedColormap,
    num_stds: float = 2.5,
    center: float | None = 0,
) -> Callable:
    """Returns a centered and normalized colormap function that takes a float as an argument and
    returns an rgba value.

    Args:
        s (pd.Series):
            a series of numeric values
        cmap (matplotlib.colors.LinearSegmentedColormap):
            matplotlib Colormap
        num_stds (float, optional):
            vmin and vmax are set to the median ± num_stds.
            Defaults to 2.5.

    Returns:
        Callable: Callable that takes a float as an argument and returns an rgba value.
    """

    if center is None:
        center = s.median()

    _std = s.std()

    vmin = center - num_stds * _std
    vmax = center + num_stds * _std

    norm = TwoSlopeNorm(vcenter=center, vmin=vmin, vmax=vmax)
    m = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)

    return m.to_rgba
