#!/usr/bin/python3
"""
Defines a python class_to_json module
"""

def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure"""
    return obj.__dict__
