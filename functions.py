# functions.py

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def divide(a: float, b: float) -> float:
    """
    Returns the division of two numbers.
    Raises ValueError if the divisor is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def is_even(number: int) -> bool:
    """Checks if an integer number is even."""
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.") 
    return number % 2 == 0