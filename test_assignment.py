# test_recursion_simple.py
import pytest
from assignment import fibonacci, count_digits, sum_digits

def detects_recursion(func):
    called_inside = {"inside": False}

    def wrapper(*args, **kwargs):
        if wrapper._active:
            called_inside["inside"] = True
        wrapper._active = True
        result = func(*args, **kwargs)
        wrapper._active = False
        return result

    wrapper._active = False
    return wrapper, called_inside

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (6, 8),
    (10, 55)
])
def test_fibonacci(n, expected):
    wrapped, state = detects_recursion(fibonacci)
    result = wrapped(n)
    assert result == expected
    assert state["inside"], "fibonacci() does not use recursion!"
    
@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (5, 1),
    (5029, 4),
    (1234567890, 10)
])
def test_count_digits(n, expected):
    wrapped, state = detects_recursion(count_digits)
    result = wrapped(n)
    assert result == expected
    assert state["inside"], "count_digits() does not use recursion!"

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (5, 5),
    (5029, 16),
    (123, 6),
    (9999, 36)
])
def test_sum_digits(n, expected):
    wrapped, state = detects_recursion(sum_digits)
    result = wrapped(n)
    assert result == expected
    assert state["inside"], "sum_digits() does not use recursion!"
