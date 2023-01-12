#!/usr/bin/python3
# 6-load_from_json_file.py
"""Defines a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Prints an Object to a text file, using a JSON representation"""
    with open(filename) as f:
        return json.load(f)
