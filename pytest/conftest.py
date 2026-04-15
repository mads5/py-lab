import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt",     # This is the custom cmd line argument
        action="store",
        default="type1",
        help="choose type1 or type2",
        choices=("type1", "type2")
    )
