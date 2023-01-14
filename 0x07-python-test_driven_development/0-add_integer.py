#!/usr/bin/python3
"""
This is the 0-add_integer  module.
The 0-add_integer module supplies one function, add_integer().

"""


def add_integer(a, b=98):
    """
    Return the addition of a and b.
    Args:
        a (int, float): the first value.
        b (int, float): the second value.
    """
    if type(a) in [int, float]:
        try:
            a = int(a)
        except Exception:
            raise TypeError("a must be an integer")
    else:
        raise TypeError("a must be an integer")

    if type(b) in [int, float]:
        try:
            b = int(b)
        except Exception:
            raise TypeError('b must be an integer')
    else:
        raise TypeError('b must be an integer')

    return a + b
