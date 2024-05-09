"""
Ten plik zawiera testy jednostkowe dla modułu utils.
"""

import pytest
import utils


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)])
def test_add(a, b, expected):
    """
    Testuje funkcję utils.add.

    Args:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.
        expected (int): Oczekiwana suma a i b.

    Asserts:
        Wynik dodawania a i b jest zgodny z oczekiwanym.
    """
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    """
    Testuje funkcję utils.subtract.

    Args:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.
        expected (int): Oczekiwana różnica a i b.

    Asserts:
        Wynik odejmowania b od a jest zgodny z oczekiwanym.
    """
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    """
    Testuje funkcję utils.multiply.

    Args:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.
        expected (int): Oczekiwany iloczyn a i b.

    Asserts:
        Wynik mnożenia a i b jest zgodny z oczekiwanym.
    """
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    """
    Testuje funkcję utils.divide.

    Args:
        a (int): Pierwsza liczba.
        b (float): Druga liczba.
        expected (float): Oczekiwany wynik dzielenia a przez b.

    Asserts:
        Wynik dzielenia a przez b jest zgodny z oczekiwanym.
    """
    result = utils.divide(a, b)
    assert result == expected
