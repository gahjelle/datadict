"""Dataclass with dictionary-like attribute access"""

# Standard library imports
import dataclasses


def dataclass(cls=None, **kwargs):
    """Add item access to attributes"""

    def wrap(cls):
        """Wrapper that adds methods and attributes to class"""

        # Create regular dataclass
        cls = dataclasses.dataclass(**kwargs)(cls)

        # Add item access
        dataclasses._set_new_attribute(cls, "__getitem__", _getitem)
        dataclasses._set_new_attribute(cls, "__setitem__", _setitem)
        dataclasses._set_new_attribute(cls, "__delitem__", _delitem)
        dataclasses._set_new_attribute(cls, "asdict", _asdict)

        return cls

    return wrap if cls is None else wrap(cls)


def _getitem(self, key):
    """Get an attribute from a dataclass using item access"""
    try:
        return getattr(self, key)
    except AttributeError:
        raise KeyError(key) from None


def _setitem(self, key, value):
    """Set an attribute on a dataclass using item access"""
    setattr(self, key, value)


def _delitem(self, key):
    """Delete an attribute on a dataclass using item access"""
    delattr(self, key)


def _asdict(self):
    """Convert the dataclass to a dictionary"""
    return dataclasses.asdict(self)
