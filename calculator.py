import pytest


# from pytest import xfail
class Calculator:

    def add(self, a, b):
        return a + b

    def division(self, a, b):
        try:
            return a / float(b)
        except ZeroDivisionError:
            return "Division to zero is not possible"


@pytest.fixture
def calculator():
    return Calculator()


@pytest.mark.xfail
def test_division(calculator):
    assert calculator.division(1, 0) == "Division to zero is not possible"


@pytest.mark.parametrize(
    "a, b, expected",
    [(3, 5, 8), (2, 2, 4), (-3, 3, 0), (100, 200, 300)])
def test_add(calculator, a, b, expected):
    result = calculator.add(a, b)
    assert result == expected
