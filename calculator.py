"""
This is my calculator.
"""

def add(*args):
    """Addition function."""
    """total = 0
    for i in args:
        total += i
    return total"""
    return float(sum(args))

def substract(x: int, y: int) -> int:
    """Substraction function."""
    return x - y
