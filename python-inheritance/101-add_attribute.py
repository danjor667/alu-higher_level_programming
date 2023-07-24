#!/usr/bin/python3
"""
define add_attr
that add an attribute if
possible
"""


def add_attribute(obj, attr, value):
    """
    add attr if possible
    """
    if not hasattr(obj, "__dict__") or hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
