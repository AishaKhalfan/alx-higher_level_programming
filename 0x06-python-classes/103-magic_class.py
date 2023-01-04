#!/usr/bin/python
import math
"""MagicClas Modules
It does exactly the same as the given Python bytecode
it contains 2 classes that return area and circumference of a circle
"""


class MagicClass():
    """MagicClass that does exactly the same as the given Python bytecode"""
    def __init__(self, radius):
        if type(radius) is not int and \
          type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius
