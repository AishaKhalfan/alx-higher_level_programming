#!/usr/bin/python3
"""
MyList Module
It inherits from List
"""


class MyList(List):
    """a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
