#!/usr/bin/python3

"""Rectangle module: This class models a square"""


class Rectangle:
    """Class definition of rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """create a property method for private instance"""
    @property
    def width(self):
        return self.__width

    """retrieve the property instance"""
    @width.setter
    def width(self, value):
        """check if width is an integer"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """create a property method for private instance"""
    @property
    def height(self):
        return self.__height

    """retrieve the property instance"""
    @height.setter
    def height(self, value):
        """check if height is an integer"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
