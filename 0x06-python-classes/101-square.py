#!/usr/bin/python3
"""Square Module"""


class Square():
    """Defines a sqaure"""

    def __init__(self, size=0, position=(0, 0)):
        """sets the necessary attributes for the Square object
        Args:
            size (int): the size of one side of the square
            position (tuple): a tuple of 2 potive ints
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrive size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """To set size of square"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """To retrieve position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """To set position of square"""
        if type(value) is tuple and len(value) is 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """"Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character in stdout"""
        if self.__size > 0:
            for x in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print("#" * self.__size)
        else:
            print()

    def __str__(self):
        """Sets the print behavior of the Square object."""
        square_str = ""

        if self.__size > 0:
            for y in range(self.__position[1]):
                square_str += '\n'
            for x in range(self.__size):
                square_str += ' ' * self.__position[0]
                square_str += '#' * self.__size + '\n'

        return square_str[:-1]
