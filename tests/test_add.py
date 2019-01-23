"""
Test the add() function of my calculator.
"""

from calculator import add

def test_addition():
    """
    Tests that the addition function works.
    """
    assert add(2, 2) == 4
