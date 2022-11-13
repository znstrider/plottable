from __future__ import annotations

from numbers import Number
from typing import Callable


def apply_string_formatter(fmt: str, val: str | Number) -> str:
    return fmt.format(val)


def apply_formatter(formatter: str | Callable, content: str | Number) -> str:
    """Applies a formatter to the content.

    Args:
        formatter (str | Callable):
            the string formatter.
            Can either be a string format, ie "{:2f}" for 2 decimal places.
            Or a Callable that is applied to the content.
        content (str | Number):
            The content to format

    Raises:
        TypeError: when formatter is not of type str or Callable.

    Returns:
        str: a formatted string
    """

    if isinstance(formatter, str):
        return apply_string_formatter(formatter, content)
    elif isinstance(formatter, Callable):
        return formatter(content)
    else:
        raise TypeError("formatter needs to be either a `Callable` or a string.")


def decimal_to_percent(val: float) -> str:
    """Formats Numbers to a string, replacing
        0 with "–"
        1 with "✓"
        values < 0.01 with "<1%" and
        values > 0.99 with ">99%"

    Args:
        val (float): numeric value to format

    Returns:
        str: formatted numeric value as string
    """
    if val == 0:
        return "–"
    elif val == 1:
        return "✓"  # "\u2713"
    elif val < 0.01:
        return "<1%"
    elif val > 0.99:
        return ">99%"
    else:
        return f"{str(round(val * 100))}%"


def tickcross(val: Number | bool) -> str:
    """formats a bool or (0, 1) value to a tick "✔" or cross "✖".

    Args:
        val (Number | bool): bool or (0, 1) value to format

    Returns:
        str: formatted value as string
    """
    if val:
        return "✔"
    else:
        return "✖"


def signed_integer(val: int) -> str:
    """formats an integer to a string that includes the sign, ie. 1 to "+1".

    Args:
        val (int): integer value to format

    Returns:
        str: formatted value as string
    """
    if val <= 0:
        return str(val)
    else:
        return f"+{val}"
