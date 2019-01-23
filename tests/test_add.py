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

def test_no_params():
    """If no params are provided return 0"""
    assert add() == 0

def test_one_two_three():
    """ Given values 1, 2, 3 as params, return 6. """
    assert add(1, 2, 3) == 6

def test_negative_values():
    """ Given values -5 and -10, the result is -15 """
    assert add(-5, -10) == -15
