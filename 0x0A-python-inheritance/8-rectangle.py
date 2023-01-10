#!/usr/bin/python3
"""BaseGeometry module
Contains a class BaseGeometry.
"""


class BaseGeometry:
    """Defines the BaseGeometry Class"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks whether a value is an integer and raises a TypeError if not
        Also checks whether a value is < 0 and raises a ValueError
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """Defines Rectangle class"""

    def __init__(self, width, height):
        """Instantiates Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
