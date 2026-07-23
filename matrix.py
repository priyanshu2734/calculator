"""
matrix.py
---------

Matrix operations for the Scientific Calculator.
"""

import numpy as np


class Matrix:
    """Provides common matrix operations."""

    @staticmethod
    def create(matrix):
        return np.array(matrix, dtype=float)

    @staticmethod
    def add(matrix1, matrix2):
        return np.add(matrix1, matrix2)

    @staticmethod
    def subtract(matrix1, matrix2):
        return np.subtract(matrix1, matrix2)

    @staticmethod
    def multiply(matrix1, matrix2):
        return np.matmul(matrix1, matrix2)

    @staticmethod
    def transpose(matrix):
        return np.transpose(matrix)

    @staticmethod
    def determinant(matrix):
        return round(np.linalg.det(matrix), 6)

    @staticmethod
    def inverse(matrix):
        det = np.linalg.det(matrix)

        if abs(det) < 1e-10:
            raise ValueError("Matrix has no inverse.")

        return np.linalg.inv(matrix)

    @staticmethod
    def rank(matrix):
        return np.linalg.matrix_rank(matrix)

    @staticmethod
    def trace(matrix):
        return np.trace(matrix)

    @staticmethod
    def identity(size):
        return np.identity(size)

    @staticmethod
    def zeros(rows, cols):
        return np.zeros((rows, cols))

    @staticmethod
    def ones(rows, cols):
        return np.ones((rows, cols))

    @staticmethod
    def scalar_multiply(matrix, scalar):
        return matrix * scalar

    @staticmethod
    def element_wise_multiply(matrix1, matrix2):
        return np.multiply(matrix1, matrix2)

    @staticmethod
    def power(matrix, power):
        return np.linalg.matrix_power(matrix, power)

    @staticmethod
    def is_square(matrix):
        return matrix.shape[0] == matrix.shape[1]

    @staticmethod
    def shape(matrix):
        return matrix.shape

    @staticmethod
    def convert_to_list(matrix):
        return matrix.tolist()