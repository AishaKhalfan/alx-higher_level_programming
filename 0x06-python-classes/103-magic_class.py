#!/usr/bin/python
"""MagicClas Modules
It does exactly the same as the given Python bytecode
it contains 2 classes that return area and circumference of a circle
"""


import math


class MagicClass():
    """MagicClass that does exactly the same as the given Python bytecode"""

    def __init__(self, radius=0):
        """sets the necessary attirbutes for the MagicClss object.
        Args:
            radius (int, float): the radius if the circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """defines the area of a circle"""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Defines the circumference of a circle"""
        return 2 * math.pi * self.__radius
