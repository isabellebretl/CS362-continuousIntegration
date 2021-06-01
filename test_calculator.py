"""
Tests for calculator app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)

    def test_subract(self):
        assert 5 == calculator.subract(10, 5)

    def test_multiply(self):
        assert 4 == calculator.multiply(2, 2)