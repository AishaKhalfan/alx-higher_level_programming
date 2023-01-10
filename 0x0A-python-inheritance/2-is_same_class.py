#!/usr/bin/python3
"""is_same_Class module.
Contains function that compares an object with an instance.
"""


def is_same_class(obj, a_class):
    """Returns true if the object is exactly an instance of
    the specified class otherwise False
    """
    return type(obj) is a_class
