#!/usr/bin/python3
# 5-text_indentation.py
"""
Defines a text_indentation function
"""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        text = text.replace(". ", ".").replace(": ", ":").replace("? ", "?")
        for i in text:
            if i == '.' or i == '?' or i == ':':
                print(i, end="")
                print("\n")
            else:
                print(i, end="")
