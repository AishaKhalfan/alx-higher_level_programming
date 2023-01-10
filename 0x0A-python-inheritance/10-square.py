#!/usr/bin/python3
"""Square module.
Contains a class Square that inherits from
Rectangle and some methods.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines the Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Checks and sets the default attributes of Square class."""
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """Sets the str behaviour."""
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        """Returns the area of the Square."""
        return self.__size * self.__size
