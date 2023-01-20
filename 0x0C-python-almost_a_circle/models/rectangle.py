#!/usr/bin/python3
"""This is the Rectangle module.
Contains the Rectangle class that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """This class inherits from Base and defines a Rectangle object.
    Attributes:
        __width (int): the width of the rectangle.
        __height (int): the height of the rectangle.
        __x (int): the horizontal (x) padding of the rectangle.
        __y (int): the vertical (y) padding of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the default attributes of the Base object
        Args:
            width (int): the wanted width of the rectangle.
            height (int): the wanted height of the rectangle.
            x (int): the wanted horizontal (x) padding of the rectangle.
            y (int): the wanted vertical (y) padding of the rectangle.
            id (int): the wanted identifier of the Base object.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Overrides the default behaviour of the __str__ method."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """Get and set the width attr of the Rectangle"""
        self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value)

    @property
    def height(self):
        """Get and set the height attr of the Rectangle"""
        self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # x attribute getter and setter
    @property
    def x(self):
        self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # y attribute getter and setter
    @property
    def y(self):
        self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
