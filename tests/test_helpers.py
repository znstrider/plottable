from plottable.helpers import _replace_lw_key


def test_replace_lw_key():
    d = {"lw": 1}

    d = _replace_lw_key(d)

    assert "lw" not in d
    assert "linewidth" in d
    assert d["linewidth"] == 1
