"""Fixtures are used for setup and teardown methods"""
import pytest
from StudentDB import StudentDBClass

'''Possible values for scope are: function(default), class, module, package and session'''
@pytest.fixture(scope="module")
def db():
    print("-----Setup------")
    db = StudentDBClass()
    db.connect("FixtureExample/FixtureData.json")
    yield db
    print("---Teardown-----")
    db.close()

def test_scott_data(db):
    scott_data = db.get_data("Scott")
    assert scott_data['id'] == 1
    assert scott_data['name'] == "Scott"
    assert scott_data["result"] == "pass"

def test_mark_data(db):
    mark_data = db.get_data("Mark")
    assert mark_data['id'] == 2
    assert mark_data['name'] == "Mark"
    assert mark_data['result'] == "fail"

