#!/usr/bin/python3
"""Rectangle Module
Contains a class that defines a rectangle
using a private instance height and weight
And a public instance area and perimeter
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

    def __repr__(self):
        """sets the repr behavior of the rectangle object"""
        return "Rectangle({:d}, {:d})".format(self.__height, self.__width)

    def __str__(self):
        """sets the print behavior of the rectangle"""
        rectangle = ""

        if self.__height > 0 and self.__width > 0:
            for x in range(self.__height):
                rectangle += '#' * self.__width + '\n'
        return rectangle[:-1]

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

    def area(self):
        """Prints the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height is 0 or self.__width is 0:
            return 0
        else:
            return (self.__height + self.__width) * 2
