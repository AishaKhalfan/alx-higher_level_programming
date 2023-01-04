#!/usr/bin/python3
"""Square module.
This module contains a class that defines a square and init method that
sets its size and checking if the given values are right. There's also an
area method that returns the area of the square.
"""


class Square():
    """Defines a square."""

    def __init__(self, size=0):
        """Sets the necessary attributes for the Square object.
        Args:
            size (int): the size of one edge of the square.
        Raises:
            TypeError: if size is not given as a number.
            ValueError: if size is less than 0.
        """
        self.size = size

    def __eq__(self, other):
        """sets the compare equality behavior of the square object
        Args:
            other(square): the square object to compare with.
        """
        if type(other) is Square:
            return self.area() == other.area()

    def __ne__(self, other):
        """sets the compare Not equality behavior of the square object
        Args:
            other(square): the square object to compare with.
        """
        if type(other) is Square:
            return self.area() != other.area()

    def __gt__(self, other):
        """sets the compare greater than behavior of the square object
        Args:
            other(square): the square object to compare with.
        """
        if type(other) is Square:
            return self.area() > other.area()

    def __ge__(self, other):
        """sets the compare greater than or equal behavior of the square object
        Args:
            other(square): the square object to compare with.
        """
        if type(other) is Square:
            return self.area() >= other.area()

    def __lt__(self, other):
        """sets the compare less than behavior of the square object
        Args:
            other(square): the square object to compare with.
        """
        if type(other) is Square:
            return self.area() < other.area()

    def __le__(self, other):
        """sets the compare less than or equality behavior of the square object
        Args:
            other(square): the square object to compare with.
        """
        if type(other) is Square:
            return self.area() <= other.area()

    @property
    def size(self):
        """Get or set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int or type(value) is float:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be a number")

    def area(self):
        """Returns the current area of the square"""
        return self.__size ** 2
