"""
utils.py

Utility functions used by the calculator.
"""

import math


def is_number(value):

    try:

        float(value)

        return True

    except ValueError:

        return False


def format_number(value):

    if isinstance(value, float):

        if value.is_integer():

            return str(int(value))

        return f"{value:.10f}".rstrip("0").rstrip(".")

    return str(value)


def degrees_to_radians(value):

    return math.radians(value)


def radians_to_degrees(value):

    return math.degrees(value)


def clamp(value, minimum, maximum):

    return max(minimum, min(value, maximum))


def safe_divide(a, b):

    if b == 0:

        raise ZeroDivisionError("Cannot divide by zero")

    return a / b


def factorial_safe(n):

    if n < 0:

        raise ValueError("Negative factorial not allowed")

    return math.factorial(int(n))