import pytest
from plottable.formatters import decimal_to_percent, signed_integer, tickcross


class TestDecimalToPercent:
    def test_decimal_to_percent_is_zero(self):
        assert decimal_to_percent(0) == "–"

    def test_decimal_to_percent_is_one(self):
        assert decimal_to_percent(1) == "✓"

    def test_decimal_to_percent_smaller_than_one(self):
        assert decimal_to_percent(0.005) == "<1%"

    def test_decimal_to_percent_bigger_than_point_ninetynine(self):
        assert decimal_to_percent(0.995) == ">99%"

    def test_decimal_to_percent_other_rounds_down(self):
        assert decimal_to_percent(0.554) == "55%"

    def test_decimal_to_percent_other_rounds_up(self):
        assert decimal_to_percent(0.555) == "56%"


@pytest.mark.parametrize(
    "input,out", [(0, "✖"), (1, "✔"), (0.0, "✖"), (True, "✔"), (False, "✖")]
)
def test_tickcross(input, out):
    assert tickcross(input) == out


def test_signed_integer():
    assert signed_integer(0) == "0"
    assert signed_integer(1) == "+1"
    assert signed_integer(-1) == "-1"
