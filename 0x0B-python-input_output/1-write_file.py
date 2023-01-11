#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        print(f.write(text))
