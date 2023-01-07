#!/usr/bin/python3
"""Rectangle Module
Contains a class that defines a rectangle
using a private instance height and weight
And a public instance area and perimeter
"""


class Rectangle():
    """defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Sets the necessary attributes for the rectangle object
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    def __str__(self):
        """sets the print behavior of the rectangle"""
        rectangle = ""

        if self.__height > 0 and self.__width > 0:
            for x in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width + '\n'

        return rectangle[:-1]

    def __repr__(self):
        """sets the repr behavior of the rectangle object"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

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

    def area(self):
        """Prints the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height is 0 or self.__width is 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with equals width and height."""
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle, or rect_1 if equals."""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    def __del__(self):
        """Sets the del behavior of the Rectangle object."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
