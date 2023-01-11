#!/usr/bin/python3
"""defines a write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
