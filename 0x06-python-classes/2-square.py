#!/usr/bin/python3
"""Square modeule.Contains a class that defines a square.
instantiation with optional size: def __init__(self, size=0)
"""


class Square():
    """Defines a sqaure."""

    def __init__(self, size=0):
        """Sets the necessary attributes for the Square object.
        Args:
            size (int): the size of one edge of the square.
        Raises:
            TypeError: if size is not given as an integer
            ValueError: if size is less than 0
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
