#!/usr/bin/python3
# 5-save_to_json_file.py
"""Defines a function that writes an Object to text
file using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Prints an Object to a text file, using a JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
