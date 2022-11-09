from numbers import Number
from typing import Callable, TypeVar

from matplotlib.colors import LinearSegmentedColormap

Cmap = TypeVar("Cmap", Callable, LinearSegmentedColormap)
Content = TypeVar("Content", str, Number)
Fmt = TypeVar("Fmt", str, Callable)
