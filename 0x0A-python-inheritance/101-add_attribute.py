#!/usr/bin/python3
"""add_attribute module
contains a function that adds a new attribute to an object
"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if its possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
