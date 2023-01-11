#!/usr/bin/python3
# 4-from_json_string.py
"""Defines a JSON-string-to-Object function."""
import json


def from_json_string(my_str):
    """Return an object represented by a JSON string"""
    return json.loads(my_str)
