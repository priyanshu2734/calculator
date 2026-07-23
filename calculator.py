"""
calculator.py
-------------

Basic mathematical operations used by the Scientific Calculator.
"""

import math


class Calculator:
    """Provides basic calculator operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    @staticmethod
    def modulus(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulus by zero.")
        return a % b

    @staticmethod
    def floor_division(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a // b

    @staticmethod
    def power(base: float, exponent: float) -> float:
        return base ** exponent

    @staticmethod
    def square(number: float) -> float:
        return number ** 2

    @staticmethod
    def cube(number: float) -> float:
        return number ** 3

    @staticmethod
    def square_root(number: float) -> float:
        if number < 0:
            raise ValueError("Square root of negative number is undefined.")
        return math.sqrt(number)

    @staticmethod
    def cube_root(number: float) -> float:
        return math.copysign(abs(number) ** (1 / 3), number)

    @staticmethod
    def reciprocal(number: float) -> float:
        if number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return 1 / number

    @staticmethod
    def percentage(value: float, percent: float) -> float:
        """
        Example:
        percentage(500, 20) -> 100
        """
        return (value * percent) / 100

    @staticmethod
    def absolute(number: float) -> float:
        return abs(number)

    @staticmethod
    def negate(number: float) -> float:
        return -number

    @staticmethod
    def factorial(number: int) -> int:
        if number < 0:
            raise ValueError("Factorial of negative number is undefined.")

        if not float(number).is_integer():
            raise ValueError("Factorial is only defined for whole numbers.")

        return math.factorial(int(number))

    @staticmethod
    def average(numbers: list[float]) -> float:
        if not numbers:
            raise ValueError("List cannot be empty.")
        return sum(numbers) / len(numbers)

    @staticmethod
    def maximum(numbers: list[float]) -> float:
        if not numbers:
            raise ValueError("List cannot be empty.")
        return max(numbers)

    @staticmethod
    def minimum(numbers: list[float]) -> float:
        if not numbers:
            raise ValueError("List cannot be empty.")
        return min(numbers)

    @staticmethod
    def round_number(number: float, digits: int = 2) -> float:
        return round(number, digits)

    @staticmethod
    def is_even(number: int) -> bool:
        return number % 2 == 0

    @staticmethod
    def is_odd(number: int) -> bool:
        return number % 2 != 0

    @staticmethod
    def gcd(a: int, b: int) -> int:
        return math.gcd(a, b)

    @staticmethod
    def lcm(a: int, b: int) -> int:
        return abs(a * b) // math.gcd(a, b)

    @staticmethod
    def clamp(value: float, minimum: float, maximum: float) -> float:
        return max(minimum, min(value, maximum))