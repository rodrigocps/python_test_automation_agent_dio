import pytest
from functions import *

def test_add_valid_inputs():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0

def test_divide_valid_inputs():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    assert divide(0, 1) == 0
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        divide(10, 0)

def test_is_even_valid_inputs():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-2) is True

def test_is_even_invalid_input():
    with pytest.raises(TypeError, match="Input must be an integer."):
        is_even(2.5)
    with pytest.raises(TypeError, match="Input must be an integer."):
        is_even("string")
    with pytest.raises(TypeError, match="Input must be an integer."):
        is_even([])