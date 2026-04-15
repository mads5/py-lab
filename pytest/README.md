# Pytest Testing Framework

This directory contains tests developed using the Pytest framework, which is a powerful tool for writing simple as well as scalable test cases in Python.

## Features of Pytest
- **Simple test writing**: Write tests using simple assert statements without any boilerplate code.
- **Fixtures**: Provides a way to create setup code that can be reused across multiple test functions.
- **Plugins**: Extend the functionality with a rich ecosystem of plugins.
- **Parameterized tests**: Easily run a test with multiple sets of parameters.

## Fixtures

Fixtures are functions that can be used to set up some context for your tests. They are defined using the `@pytest.fixture` decorator and can be shared across tests. Below is an example:

```python
import pytest

@pytest.fixture
def sample_fixture():
    # Setup code
    return "fixture data"  

def test_example(sample_fixture):
    assert sample_fixture == "fixture data"
```
## Test Examples
### Basic test
```python
def test_addition():
    assert 1 + 1 == 2
```
### Using Fixtures
```python
def test_with_fixture(sample_fixture):
    assert sample_fixture == "fixture data"
```
### Parameterized Test
```python
@pytest.mark.parametrize("input, expected", [(1, 2), (2, 3), (3, 4)])
def test_increment(input, expected):
    assert input + 1 == expected
```

## Running Tests
To run the tests in this directory, execute:
```
pytest
```

## Conclusion
Utilize the tests in this directory to ensure the quality and functionality of your code by leveraging the capabilities of the Pytest framework.
