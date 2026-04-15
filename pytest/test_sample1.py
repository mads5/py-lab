import pytest

# Basic Assertion
def inc(x):
    return x + 1

def test_inc():
    assert inc(4) == 5

# Assertion in Exceptions
def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        1/0

def test_maxrecursions():
    with pytest.raises(RuntimeError) as exeinfo:
        def f():
            f()
        f()
    assert "maximum recursion" in str(exeinfo.value)
    assert "RecursionError" in str(exeinfo.type)

def raise_exception():
    raise ValueError("Number 123 is invalid")

def test_exeception_regex():
    with pytest.raises(ValueError, match='123'):
        raise_exception()