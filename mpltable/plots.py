from statistics import mean
from typing import Any, Callable, Dict, Tuple

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import BoxStyle, Circle, FancyBboxPatch, Rectangle, Wedge
from PIL import Image


def image(ax: matplotlib.axes.Axes, path: str):
    img = plt.imread(path)
    im = ax.imshow(img)
    im.set_clip_on(False)
    ax.axis("off")
    return im


def monochrome_image(ax: matplotlib.axes.Axes, path: str):
    img = Image.open(path).convert("LA")
    im = ax.imshow(img)
    im.set_clip_on(False)
    ax.axis("off")
    return im


def circled_image(ax: matplotlib.axes.Axes, path: str):
    img = plt.imread(path)
    im = ax.imshow(img)
    ax.axis("off")

    radius = min(max(ax.get_xlim()), max(ax.get_ylim())) / 2
    center = (mean(ax.get_xlim()), mean(ax.get_ylim()))
    circle = Circle(center, radius, transform=ax.transData)
    im.set_clip_on(True)
    im.set_clip_path(circle)

    ax.set_aspect("equal")

    return im


def bar(
    ax: matplotlib.axes.Axes,
    val: float,
    xlim: Tuple[float, float] = (0, 1),
    cmap: matplotlib.colors.Colormap = None,
    plot_bg_bar: bool = False,
    annotate: bool = False,
    text_kwargs: Dict[str, Any] = {},
    formatter: Callable = None,
    **kwargs,
):

    if "color" in kwargs:
        color = kwargs.pop("color")
    else:
        color = "C1"

    if cmap is not None:
        color = cmap(float(val))

    if plot_bg_bar:
        ax.barh(
            0.5,
            xlim[1],
            left=xlim[0],
            fc="None",
            ec=plt.rcParams["text.color"],
            **kwargs,
            zorder=0.1,
        )

    bar = ax.barh(0.5, val, fc=color, ec="None", **kwargs, zorder=0.05)

    if annotate:
        if val < 0.5 * xlim[1]:
            ha = "left"
            x = val + 0.025 * abs(xlim[1] - xlim[0])
        else:
            ha = "right"
            x = val - 0.025 * abs(xlim[1] - xlim[0])

        if formatter is not None:
            val = formatter(val)

        ax.text(x, 0.5, val, ha=ha, va="center", **text_kwargs, zorder=0.3)

    ax.axis("off")
    ax.set_xlim(
        xlim[0] - 0.025 * abs(xlim[1] - xlim[0]),
        xlim[1] + 0.025 * abs(xlim[1] - xlim[0]),
    )
    ax.set_ylim(0, 1)

    return bar


def percentile_bars(
    ax: matplotlib.axes.Axes,
    val: float,
    color: str = None,
    faded_color: str = None,
    cmap: matplotlib.colors.Colormap = None,
    is_pct=False,
    rect_kw: Dict[str, Any] = {},
):

    _rect_kw = {
        "linewidth": 2.5,
        "boxstyle": BoxStyle("Round", pad=0, rounding_size=0.05),
    }

    _rect_kw.update(rect_kw)

    edgecolor = ax.get_facecolor()

    if faded_color is None:
        faded_color = ax.get_facecolor()

    if is_pct is False:
        val = val / 100

    if cmap is not None:
        color = cmap(val)
    elif color is None:
        color = "C1"

    value_patch = Rectangle(
        xy=(0, 0), width=val, height=1, color="w", alpha=0.75, transform=ax.transData
    )

    bg_rects = []
    rects = []

    for x in np.linspace(0, 0.9, 10):

        bg_rect = FancyBboxPatch(
            xy=(x, 0),
            width=0.1,
            height=1,
            facecolor=faded_color,
            edgecolor=edgecolor,
            alpha=1,
            **_rect_kw,
            zorder=0.1,
        )
        bg_rects.append(bg_rect)
        ax.add_patch(bg_rect)

        rect = FancyBboxPatch(
            xy=(x, 0),
            width=0.1,
            height=1,
            facecolor=color,
            edgecolor=edgecolor,
            **_rect_kw,
            zorder=0.2,
        )
        rects.append(rect)
        ax.add_patch(rect)
        rect.set_clip_path(value_patch)

    ax.axis("off")

    return rects


def percentile_stars(
    ax: matplotlib.axes.Axes,
    val: float,
    n_stars: int = 5,
    color: str = "orange",
    faded_color: str = None,
    is_pct: bool = False,
    padding: float = 0.1,
    **kwargs,
):
    if faded_color is None:
        faded_color = ax.get_facecolor()

    if is_pct is False:
        val = val / 100

    bounds = np.linspace(0, 1, n_stars + 1)
    xs = (bounds[:-1] + bounds[1:]) / 2
    ys = n_stars * [0.5]

    value_patch = Rectangle(
        xy=(0, 0), width=val, height=1, color="w", alpha=0.75, transform=ax.transData
    )

    if "s" not in kwargs:
        kwargs["s"] = 200

    ax.scatter(x=xs, y=ys, color=faded_color, marker="*", zorder=0.2, alpha=1, **kwargs)
    sc = ax.scatter(x=xs, y=ys, color=color, marker="*", zorder=0.2, **kwargs)
    sc.set_clip_path(value_patch)

    ax.set_ylim(0 - padding, 1 + padding)
    ax.set_xlim(0 - padding, 1 + padding)
    ax.axis("off")

    return sc


def progress_donut(
    ax: matplotlib.axes.Axes,
    val: float,
    radius: float = 0.45,
    color: str = None,
    background_color: str = None,
    width: float = 0.05,
    is_pct: bool = False,
    textprops: Dict[str, Any] = {},
    formatter: Callable = None,
    **kwargs,
):

    if color is None:
        color = "C1"

    if is_pct is False:
        val = val / 100

    if background_color is not None:
        bg_wedge = Wedge(
            (0.5, 0.5),
            radius,
            90,
            360 + 90,
            width=width,
            color=background_color,
            **kwargs,
        )
        ax.add_patch(bg_wedge)

    wedge = Wedge(
        (0.5, 0.5), radius, 90, 90 + val * 360, width=width, color=color, **kwargs
    )
    ax.add_patch(wedge)
    ax.set_aspect("equal")

    if formatter is not None:
        val = formatter(val)

    ax.text(0.5, 0.5, val, ha="center", va="center", **textprops)
    ax.axis("off")
