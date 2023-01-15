#!/usr/bin/python3
"""
This is the say_my_name module
It supplies one function say_my_name()
"""


def say_my_name(first_name, last_name=""):
    """
    Print: My name is <first name> <last name>
    Args:
        first_name (str): The first name
        last_name (str): The second name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("lastt_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
