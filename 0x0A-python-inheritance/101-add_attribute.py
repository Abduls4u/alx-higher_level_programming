#!/usr/bin/python3
''' A module that contains a function that adds attributes.
Usage:
    ./101-add_atttibute.py
Author:
    Abdulsalam Abdulsomad .A. - January 22nd, 2023.
Assistance - @Betascribbles
'''


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.
    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
