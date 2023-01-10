#!/usr/bin/python3
"""Rectangle module
Contains a class Rectangle that inherits from
BaseGeometry and some methods.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines Rectangle class"""

    def __init__(self, width, height):
        """Instantiates Rectangle"""
        self.integer_validator("width", self.__width)
        self.__width = width
        self.integer_validator("height", self.__height)
        self.__height = height

    def __str__(self):
        """Sets the str behavior."""
        return "[Rectangle] + {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """implementing area method"""
        return self.__width * self.__height
