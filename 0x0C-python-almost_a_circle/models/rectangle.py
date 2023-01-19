#!/usr/bin/python
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

    def __init__(self, width, height, x=0, y=0, id=None)
        """Initializes the default attributes of the Base object
        Args:
            width (int): the wanted width of the rectangle.
            height (int): the wanted height of the rectangle.
            x (int): the wanted horizontal (x) padding of the rectangle.
            y (int): the wanted vertical (y) padding of the rectangle.
            id (int): the wanted identifier of the Base object.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get and set the width attr of the Rectangle"""
        self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            self.__width = value
        else:
            raise TypeError("")

    @property
    def height(self):
        """Get and set the width attr of the Rectangle"""
        self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            self.__height = value
        else:
            raise TypeError("")
