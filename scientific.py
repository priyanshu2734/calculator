"""
scientific.py
-------------

Scientific mathematical functions for the calculator.
"""

import math


class Scientific:
    """Scientific calculator operations."""

    # -----------------------------
    # Constants
    # -----------------------------

    @staticmethod
    def pi() -> float:
        return math.pi

    @staticmethod
    def e() -> float:
        return math.e

    # -----------------------------
    # Trigonometry (Degrees)
    # -----------------------------

    @staticmethod
    def sin(angle: float) -> float:
        return math.sin(math.radians(angle))

    @staticmethod
    def cos(angle: float) -> float:
        return math.cos(math.radians(angle))

    @staticmethod
    def tan(angle: float) -> float:
        return math.tan(math.radians(angle))

    # -----------------------------
    # Inverse Trigonometry
    # Returns answer in Degrees
    # -----------------------------

    @staticmethod
    def asin(value: float) -> float:
        return math.degrees(math.asin(value))

    @staticmethod
    def acos(value: float) -> float:
        return math.degrees(math.acos(value))

    @staticmethod
    def atan(value: float) -> float:
        return math.degrees(math.atan(value))

    # -----------------------------
    # Hyperbolic Functions
    # -----------------------------

    @staticmethod
    def sinh(value: float) -> float:
        return math.sinh(value)

    @staticmethod
    def cosh(value: float) -> float:
        return math.cosh(value)

    @staticmethod
    def tanh(value: float) -> float:
        return math.tanh(value)

    # -----------------------------
    # Logarithms
    # -----------------------------

    @staticmethod
    def log(value: float) -> float:
        if value <= 0:
            raise ValueError("Logarithm undefined.")
        return math.log10(value)

    @staticmethod
    def ln(value: float) -> float:
        if value <= 0:
            raise ValueError("Natural logarithm undefined.")
        return math.log(value)

    @staticmethod
    def log2(value: float) -> float:
        if value <= 0:
            raise ValueError("Logarithm undefined.")
        return math.log2(value)

    # -----------------------------
    # Exponential
    # -----------------------------

    @staticmethod
    def exp(value: float) -> float:
        return math.exp(value)

    # -----------------------------
    # Powers & Roots
    # -----------------------------

    @staticmethod
    def power(base: float, exponent: float) -> float:
        return math.pow(base, exponent)

    @staticmethod
    def square(value: float) -> float:
        return value ** 2

    @staticmethod
    def cube(value: float) -> float:
        return value ** 3

    @staticmethod
    def square_root(value: float) -> float:
        if value < 0:
            raise ValueError("Square root undefined.")
        return math.sqrt(value)

    @staticmethod
    def cube_root(value: float) -> float:
        return math.copysign(abs(value) ** (1 / 3), value)

    # -----------------------------
    # Factorial
    # -----------------------------

    @staticmethod
    def factorial(value: int) -> int:
        if value < 0:
            raise ValueError("Factorial undefined.")

        if not float(value).is_integer():
            raise ValueError("Only whole numbers allowed.")

        return math.factorial(int(value))

    # -----------------------------
    # Combinatorics
    # -----------------------------

    @staticmethod
    def npr(n: int, r: int) -> int:
        return math.perm(n, r)

    @staticmethod
    def ncr(n: int, r: int) -> int:
        return math.comb(n, r)

    # -----------------------------
    # Miscellaneous
    # -----------------------------

    @staticmethod
    def degrees_to_radians(angle: float) -> float:
        return math.radians(angle)

    @staticmethod
    def radians_to_degrees(angle: float) -> float:
        return math.degrees(angle)

    @staticmethod
    def absolute(value: float) -> float:
        return abs(value)

    @staticmethod
    def ceil(value: float) -> int:
        return math.ceil(value)

    @staticmethod
    def floor(value: float) -> int:
        return math.floor(value)

    @staticmethod
    def truncate(value: float) -> int:
        return math.trunc(value)

    @staticmethod
    def reciprocal(value: float) -> float:
        if value == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return 1 / value

    @staticmethod
    def percentage(value: float, percent: float) -> float:
        return (value * percent) / 100
    """
scientific.py
-------------

Scientific mathematical functions for the calculator.
"""

import math


class Scientific:
    """Scientific calculator operations."""

    # -----------------------------
    # Constants
    # -----------------------------

    @staticmethod
    def pi() -> float:
        return math.pi

    @staticmethod
    def e() -> float:
        return math.e

    # -----------------------------
    # Trigonometry (Degrees)
    # -----------------------------

    @staticmethod
    def sin(angle: float) -> float:
        return math.sin(math.radians(angle))

    @staticmethod
    def cos(angle: float) -> float:
        return math.cos(math.radians(angle))

    @staticmethod
    def tan(angle: float) -> float:
        return math.tan(math.radians(angle))

    # -----------------------------
    # Inverse Trigonometry
    # Returns answer in Degrees
    # -----------------------------

    @staticmethod
    def asin(value: float) -> float:
        return math.degrees(math.asin(value))

    @staticmethod
    def acos(value: float) -> float:
        return math.degrees(math.acos(value))

    @staticmethod
    def atan(value: float) -> float:
        return math.degrees(math.atan(value))

    # -----------------------------
    # Hyperbolic Functions
    # -----------------------------

    @staticmethod
    def sinh(value: float) -> float:
        return math.sinh(value)

    @staticmethod
    def cosh(value: float) -> float:
        return math.cosh(value)

    @staticmethod
    def tanh(value: float) -> float:
        return math.tanh(value)

    # -----------------------------
    # Logarithms
    # -----------------------------

    @staticmethod
    def log(value: float) -> float:
        if value <= 0:
            raise ValueError("Logarithm undefined.")
        return math.log10(value)

    @staticmethod
    def ln(value: float) -> float:
        if value <= 0:
            raise ValueError("Natural logarithm undefined.")
        return math.log(value)

    @staticmethod
    def log2(value: float) -> float:
        if value <= 0:
            raise ValueError("Logarithm undefined.")
        return math.log2(value)

    # -----------------------------
    # Exponential
    # -----------------------------

    @staticmethod
    def exp(value: float) -> float:
        return math.exp(value)

    # -----------------------------
    # Powers & Roots
    # -----------------------------

    @staticmethod
    def power(base: float, exponent: float) -> float:
        return math.pow(base, exponent)

    @staticmethod
    def square(value: float) -> float:
        return value ** 2

    @staticmethod
    def cube(value: float) -> float:
        return value ** 3

    @staticmethod
    def square_root(value: float) -> float:
        if value < 0:
            raise ValueError("Square root undefined.")
        return math.sqrt(value)

    @staticmethod
    def cube_root(value: float) -> float:
        return math.copysign(abs(value) ** (1 / 3), value)

    # -----------------------------
    # Factorial
    # -----------------------------

    @staticmethod
    def factorial(value: int) -> int:
        if value < 0:
            raise ValueError("Factorial undefined.")

        if not float(value).is_integer():
            raise ValueError("Only whole numbers allowed.")

        return math.factorial(int(value))

    # -----------------------------
    # Combinatorics
    # -----------------------------

    @staticmethod
    def npr(n: int, r: int) -> int:
        return math.perm(n, r)

    @staticmethod
    def ncr(n: int, r: int) -> int:
        return math.comb(n, r)

    # -----------------------------
    # Miscellaneous
    # -----------------------------

    @staticmethod
    def degrees_to_radians(angle: float) -> float:
        return math.radians(angle)

    @staticmethod
    def radians_to_degrees(angle: float) -> float:
        return math.degrees(angle)

    @staticmethod
    def absolute(value: float) -> float:
        return abs(value)

    @staticmethod
    def ceil(value: float) -> int:
        return math.ceil(value)

    @staticmethod
    def floor(value: float) -> int:
        return math.floor(value)

    @staticmethod
    def truncate(value: float) -> int:
        return math.trunc(value)

    @staticmethod
    def reciprocal(value: float) -> float:
        if value == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return 1 / value

    @staticmethod
    def percentage(value: float, percent: float) -> float:
        return (value * percent) / 100