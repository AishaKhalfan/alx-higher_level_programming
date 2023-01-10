#!/usr/bin/python3
"""MyInt module
inherits from int
"""


class MyInt(int):
    """Defines MyInt class that inherits from int"""

    def __init__(self, value):
        """Initiates the MyInt class"""
        self.value = value

    def __eq__(self, other):
        """Defines Rebel __eq__ operator inverted"""
        return self.value != other

    def __ne__(self, other):
        """Defines rebel __ne__ operator inverted"""
        return self.value == other
