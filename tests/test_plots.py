import pytest
from plottable.plots import sparklines
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

@pytest.fixture
def sparkline_single():
    return sparklines(plt.gca(), 
                     [10,12,14,16,18]
                     )


@pytest.fixture
def sparkline_multiple():
    return sparklines(plt.gca(), 
                     [[10,12,14,16,18], 
                      [20,40,60,80,100]],
                      line_kwargs=[{"color": 'red', 'lw': 1}, 
                                   {"color": 'dodgerblue'}]
                     )


class TestSingleSparkline:
    def test_sparkline_single_type(self, sparkline_single):
        assert isinstance(sparkline_single, list)

    def test_sparkline_single_len(self, sparkline_single):
        assert len(sparkline_single) == 1

    def test_sparkline_single_inner_type(self, sparkline_single):
        assert isinstance(sparkline_single[0], Line2D)


class TestMultipleSparklines:
    def test_sparklines_multiple(self, sparkline_multiple):
        assert len(sparkline_multiple) == 2

    def test_sparklines_multiple_kwargs(self, sparkline_multiple):
        assert sparkline_multiple[1].get_color() == 'dodgerblue'
