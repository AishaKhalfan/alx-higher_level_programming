#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """Reads a text file"""
    with open("my_file_0.txt", encoding="utf-8") as myFile:
        print(myFile.read())
