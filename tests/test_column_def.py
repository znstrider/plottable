import pytest
from plottable.column_def import ColumnDefinition, _filter_none_values


@pytest.fixture
def col_def() -> ColumnDefinition:
    return ColumnDefinition(name="col", title="Column")


def test_filter_none_values():
    d = {"a": 1, "b": {}, "c": None}
    assert _filter_none_values(d) == {"a": 1, "b": {}}


def test_column_definition_as_dict(col_def):
    assert col_def._asdict() == {
        "name": "col",
        "title": "Column",
        "width": 1,
        "textprops": {},
        "formatter": None,
        "cmap": None,
        "text_cmap": None,
        "group": None,
        "plot_fn": None,
        "plot_kw": {},
        "border": None,
    }


def test_column_definition_as_non_none_dict(col_def):
    assert col_def._as_non_none_dict() == {
        "name": "col",
        "title": "Column",
        "width": 1,
        "textprops": {},
        "plot_kw": {},
    }
