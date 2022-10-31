import matplotlib
import pandas as pd
from plottable.cmap import normed_cmap


def test_normed_cmap():
    s = pd.Series(list(range(0, 11)))
    cmap_fn = normed_cmap(s, matplotlib.cm.PiYG)
    assert cmap_fn(10) == (
        0.49034986543637066,
        0.7307958477508651,
        0.24998077662437523,
        1.0,
    )
    assert cmap_fn(5) == (
        0.9673202614379085,
        0.968473663975394,
        0.9656286043829296,
        1.0,
    )
    assert cmap_fn(0) == (
        0.8667435601691658,
        0.45251826220684355,
        0.6748173779315648,
        1.0,
    )


def test_normed_cmap_three_stds():
    s = pd.Series(list(range(0, 11)))
    cmap_fn = normed_cmap(s, matplotlib.cm.PiYG, num_stds=3)
    assert cmap_fn(10) == (
        0.6032295271049597,
        0.8055363321799309,
        0.3822376009227222,
        1.0,
    )
    assert cmap_fn(5) == (
        0.9673202614379085,
        0.968473663975394,
        0.9656286043829296,
        1.0,
    )
    assert cmap_fn(0) == (
        0.9056516724336793,
        0.5829296424452133,
        0.7635524798154556,
        1.0,
    )
