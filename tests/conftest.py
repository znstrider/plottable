import numpy as np
import pandas as pd
import pytest
from mpltable.cell import Cell, SubplotCell, TableCell, TextCell
from mpltable.plots import percentile_bars
from mpltable.table import Table


@pytest.fixture
def default_cell() -> Cell:
    return Cell(xy=(0, 0))


@pytest.fixture
def custom_cell() -> Cell:
    return Cell(xy=(1, 2), width=3, height=4)


@pytest.fixture
def table_cell() -> TableCell:
    return TableCell(
        xy=(1, 2), content="String Content", row_idx=1, col_idx=2, width=3, height=4
    )


@pytest.fixture
def text_cell() -> TextCell:
    return TextCell(
        xy=(1, 2), content="String Content", row_idx=1, col_idx=2, width=3, height=4
    )


@pytest.fixture
def subplot_cell() -> SubplotCell:
    return SubplotCell(
        xy=(0, 0),
        content=60,
        row_idx=0,
        col_idx=0,
        plot_fn=percentile_bars,
        width=2,
        height=1,
    )


@pytest.fixture
def df() -> pd.DataFrame:
    return pd.DataFrame(
        np.random.random((10, 5)), columns=["A", "B", "C", "D", "E"]
    ).round(2)


@pytest.fixture
def table(df) -> Table:
    return Table(df)
