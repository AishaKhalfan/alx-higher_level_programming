#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """Prints the content of a UTF8 text file to stdout"""
    with open("my_file_0.txt", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
