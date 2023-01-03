#!/usr/bin/python3
"""Rectangle Module
Contains a class that defines a rectangle
using a private instance height and weight
"""


class Rectangle():
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Sets the necessary attributes for the rectangle object
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """Retrieves height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """To set height of rectangle"""
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """Retrieves width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """To set width of rectangle"""
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
