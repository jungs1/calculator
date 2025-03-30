"""Unit tests for the Calculator class."""

import pytest
from calculator.app import Calculator


class TestCalculator:
    """Test suite for the Calculator class."""

    def setup_method(self):
        """Set up a Calculator instance before each test."""
        self.calc = Calculator()

    def test_add(self):
        """Test the add method."""
        assert self.calc.add(1, 2) == 3
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(-1, -1) == -2
        assert self.calc.add(0, 0) == 0

    def test_subtract(self):
        """Test the subtract method."""
        assert self.calc.subtract(3, 2) == 1
        assert self.calc.subtract(1, 1) == 0
        assert self.calc.subtract(-1, -1) == 0
        assert self.calc.subtract(0, 5) == -5

    def test_multiply(self):
        """Test the multiply method."""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(-2, -3) == 6
        assert self.calc.multiply(0, 5) == 0

    def test_divide(self):
        """Test the divide method."""
        assert self.calc.divide(6, 3) == 2
        assert self.calc.divide(6, 2) == 3
        assert self.calc.divide(0, 5) == 0
        assert self.calc.divide(-6, 3) == -2
        assert self.calc.divide(6, -3) == -2

    def test_divide_by_zero(self):
        """Test that dividing by zero raises a ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(5, 0)
