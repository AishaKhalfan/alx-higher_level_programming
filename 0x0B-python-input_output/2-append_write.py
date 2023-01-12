#!/usr/bin/python3
""""Defines a function that appends astring at the end of a text file UTF8"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text fiel"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
