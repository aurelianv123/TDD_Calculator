"""
Test the add() function of my calculator.
"""

from calculator import add, substract

def test_addition():
    """
    Tests that the addition function works.
    """
    assert add(2, 2) == 4

def test_five_plus_ten():
    """
    Tests that the addition function works and returns 15.
    """
    assert add(5, 10) == 15

def test_substraction():
    """
    Tests that the substraction function works.
    """
    assert substract(10, 2) == 8
