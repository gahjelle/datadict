"""Test that DataDict dataclasses behaves as expected"""
import pytest
from datadict import dataclass


@dataclass
class Point:
    """Basic dataclass used for tests"""

    x: int
    y: int


@pytest.fixture
def point():
    """Instance of dataclass used in tests"""
    return Point(x=1, y=2)


def test_attribute_access(point):
    """Test that dataclass attributes can still be accessed as regular attributes"""
    assert point.x == 1


def test_item_access(point):
    """Test that dataclass attributes can also be accessed using item access"""
    assert point["x"] == 1


def test_item_access_keyerror(point):
    """Test that item access raises KeyError for unknown attributes"""
    with pytest.raises(KeyError):
        point["z"]


def test_set_existing_item(point):
    """Test that an existing attribute can be overwritten using item access"""
    point["x"] = 3

    assert point.x == 3


def test_set_new_item(point):
    """Test that a new attribute can be added using item access"""
    point["z"] = 3

    assert point.z == 3


def test_deleting_item(point):
    """Test that an attribute can be deleted using item access"""
    del point["x"]

    with pytest.raises(AttributeError):
        point.x


def test_access_dataclass_as_dictionary(point):
    """Test that dataclass can be converted to a dictionary"""
    pt_dict = point.asdict()

    assert pt_dict == {"x": 1, "y": 2}
