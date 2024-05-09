"""
Moduł utils zawiera kilka funkcji matematycznych.
"""

def add(a: int, b: int) -> int:
    """
    Dodaje dwie liczby całkowite i zwraca wynik.

    Args:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.

    Returns:
        int: Suma a i b.
    """
    return a + b

def subtract(a: int, b: int) -> int:
    """
    Odejmuje drugą liczbę od pierwszej i zwraca wynik.

    Args:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.

    Returns:
        int: Różnica a i b.
    """
    return a - b

def multiply(a: int, b: int) -> int:
    """
    Mnoży dwie liczby i zwraca wynik.

    Args:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.

    Returns:
        int: Iloczyn a i b.
    """
    return a * b

def divide(a: int, b: float) -> float:
    """
    Dzieli pierwszą liczbę przez drugą i zwraca wynik.

    Args:
        a (int): Pierwsza liczba.
        b (float): Druga liczba.

    Returns:
        float: Wynik dzielenia a przez b.

    Raises:
        ValueError: Jeśli b jest równe 0.
    """
    if b == 0:
        raise ValueError("Division by zero is undefined")
    return a / b
