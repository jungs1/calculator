"""Simple calculator module."""


class Calculator:
    """Basic calculator implementation with add, subtract, multiply, and divide operations."""

    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a and return the result."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        return a * b

    def divide(self, a, b):
        """Divide a by b and return the result.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            float: Result of division

        Raises:
            ZeroDivisionError: If b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
