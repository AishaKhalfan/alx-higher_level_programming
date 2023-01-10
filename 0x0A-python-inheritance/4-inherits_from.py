#!/usr/bin/python3
"""inherits_from module.
Contains a function that compares whether an object is an
instance of a class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """Inherits from"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
