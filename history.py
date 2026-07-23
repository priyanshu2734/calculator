"""
history.py
----------

Stores and manages calculator history.
"""

from datetime import datetime


class HistoryManager:
    """Manages calculation history."""

    def __init__(self):
        self.history = []

    def add(self, expression: str, result):
        """Add a calculation to history."""

        self.history.append({
            "time": datetime.now().strftime("%H:%M:%S"),
            "expression": expression,
            "result": result
        })

    def get_all(self):
        """Return all history."""
        return self.history

    def clear(self):
        """Clear history."""
        self.history.clear()

    def last(self):
        """Return last calculation."""
        if self.history:
            return self.history[-1]
        return None

    def total(self):
        """Return total calculations."""
        return len(self.history)

    def save(self, filename="history.txt"):
        """Save history to a file."""

        with open(filename, "w", encoding="utf-8") as file:

            for item in self.history:

                file.write(
                    f"[{item['time']}] "
                    f"{item['expression']} = "
                    f"{item['result']}\n"
                )

    def load(self, filename="history.txt"):

        try:

            with open(filename, "r", encoding="utf-8") as file:

                return file.readlines()

        except FileNotFoundError:

            return []