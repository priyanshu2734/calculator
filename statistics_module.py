"""
statistics_module.py
--------------------

Statistical operations for the Scientific Calculator.
"""

import statistics
import math


class Statistics:

    @staticmethod
    def mean(numbers):
        """Returns the mean (average)."""
        return statistics.mean(numbers)

    @staticmethod
    def median(numbers):
        """Returns the median."""
        return statistics.median(numbers)

    @staticmethod
    def mode(numbers):
        """Returns the mode."""
        try:
            return statistics.mode(numbers)
        except statistics.StatisticsError:
            return "No unique mode"

    @staticmethod
    def variance(numbers):
        """Returns the sample variance."""
        if len(numbers) < 2:
            raise ValueError("At least two values are required.")
        return statistics.variance(numbers)

    @staticmethod
    def standard_deviation(numbers):
        """Returns the sample standard deviation."""
        if len(numbers) < 2:
            raise ValueError("At least two values are required.")
        return statistics.stdev(numbers)

    @staticmethod
    def population_variance(numbers):
        """Returns the population variance."""
        return statistics.pvariance(numbers)

    @staticmethod
    def population_standard_deviation(numbers):
        """Returns the population standard deviation."""
        return statistics.pstdev(numbers)

    @staticmethod
    def maximum(numbers):
        """Returns the largest value."""
        return max(numbers)

    @staticmethod
    def minimum(numbers):
        """Returns the smallest value."""
        return min(numbers)

    @staticmethod
    def data_range(numbers):
        """Returns the range of the data."""
        return max(numbers) - min(numbers)

    @staticmethod
    def summation(numbers):
        """Returns the sum of all values."""
        return sum(numbers)

    @staticmethod
    def count(numbers):
        """Returns the total number of values."""
        return len(numbers)

    @staticmethod
    def geometric_mean(numbers):
        """Returns the geometric mean."""
        return statistics.geometric_mean(numbers)

    @staticmethod
    def harmonic_mean(numbers):
        """Returns the harmonic mean."""
        return statistics.harmonic_mean(numbers)

    @staticmethod
    def root_mean_square(numbers):
        """Returns the RMS (Root Mean Square)."""
        return math.sqrt(sum(x ** 2 for x in numbers) / len(numbers))