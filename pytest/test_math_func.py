import math_func
import pytest
import sys

#@pytest.mark.skip("Do not add number")
def test_add():
    assert math_func.add(5, 5) == 10
    assert math_func.add(9, 3) > 10
    assert math_func.add(4) == 5

#@pytest.mark.number
def test_product():
    assert math_func.product(4, 4) == 16
    assert math_func.product(9) < 20

@pytest.mark.skipif(sys.version_info < (3, 3), reason="do not run tests for python versions under 3.3")
def test_add_strings():
    result = math_func.add("Hello", " World")
    assert result == "Hello World"
    print(sys.version_info, "------")

#@pytest.mark.string
def test_product_strings():
    result = math_func.product("Banana ")
    assert result == "Banana Banana "

def test_add_float():
    result = math_func.add(10.2, 4.5)
    assert result < 20.3


@pytest.mark.parametrize('param1, param2, result', 
[
    (8, 8, 16),
    ("Hello ", "World", "Hello World"),
    (10.5,25.5, 36)
])
def test_addition(param1, param2, result):
    assert math_func.add(param1, param2) == result

"""Running commands with different flags:
pytest
pytest -v
pytest -v -k "strings and add" 
pytest -v -k "strings or add" 
pytest -v -m number : Execute the tests with specified marker "number" here
pytest -v -x : As soon as First failure occurs, test stops without further execution
pytest -v -x --tb=no : No stack trace printed for the failure
pytest -v --maxfail=2 : If max two failure occurs, immediately stop the test based on maxfail value
pytest -v -s : If you want to execute any print statements alongwith tests
pytest -v --capture=no : works the same as -s flag above
pytest -q : Quiet mode, will not show detailed info on pass/failed tests
pytest -v -k addition : Running parametrized tests - call the function only once with multiple inputs
pytest --junit-xml=result : Generate Junit XML file with filename result
pytest --cmdopt=type3 : cmdopt is a customd efined cmd line opt defined in conftest
"""