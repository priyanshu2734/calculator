"""
memory.py

Implements calculator memory functions.
"""


class Memory:

    def __init__(self):

        self.value = 0

    def clear(self):

        self.value = 0

    def store(self, number):

        self.value = float(number)

    def recall(self):

        return self.value

    def add(self, number):

        self.value += float(number)

    def subtract(self, number):

        self.value -= float(number)

    def multiply(self, number):

        self.value *= float(number)

    def divide(self, number):

        self.value /= float(number)

    def percentage(self):

        return self.value / 100

    def square(self):

        return self.value ** 2

    def cube(self):

        return self.value ** 3

    def square_root(self):

        return self.value ** 0.5

    def reciprocal(self):

        return 1 / self.value