"""
equations.py
------------

Equation solver module for the Scientific Calculator.
"""

import math


class EquationSolver:
    """Solves common algebraic equations."""

    @staticmethod
    def solve_linear(a: float, b: float):
        """
        Solves:
            ax + b = 0
        """

        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero.")

        x = -b / a

        return {"x": round(x, 6)}

    @staticmethod
    def solve_quadratic(a: float, b: float, c: float):
        """
        Solves:
            ax² + bx + c = 0
        """

        if a == 0:
            return EquationSolver.solve_linear(b, c)

        discriminant = b ** 2 - 4 * a * c

        if discriminant > 0:

            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)

            return {
                "type": "Real and Distinct",
                "x1": round(x1, 6),
                "x2": round(x2, 6)
            }

        elif discriminant == 0:

            x = -b / (2 * a)

            return {
                "type": "Real and Equal",
                "x": round(x, 6)
            }

        else:

            real = -b / (2 * a)
            imaginary = math.sqrt(-discriminant) / (2 * a)

            return {
                "type": "Complex",
                "x1": complex(round(real, 6), round(imaginary, 6)),
                "x2": complex(round(real, 6), -round(imaginary, 6))
            }

    @staticmethod
    def discriminant(a: float, b: float, c: float):
        """
        Returns the discriminant of a quadratic equation.
        """

        return b ** 2 - 4 * a * c

    @staticmethod
    def is_quadratic(a: float):
        """
        Checks if equation is quadratic.
        """

        return a != 0

    @staticmethod
    def vertex(a: float, b: float, c: float):
        """
        Returns the vertex of a quadratic equation.
        """

        if a == 0:
            raise ValueError("Not a quadratic equation.")

        x = -b / (2 * a)

        y = a * x ** 2 + b * x + c

        return (
            round(x, 6),
            round(y, 6)
        )

    @staticmethod
    def axis_of_symmetry(a: float, b: float):
        """
        Returns the axis of symmetry.
        """

        if a == 0:
            raise ValueError("Not a quadratic equation.")

        return round(-b / (2 * a), 6)