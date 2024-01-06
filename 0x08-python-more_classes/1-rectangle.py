#!/usr/bin/python3

"""Rectangle module: This class models a Rectangle"""


class Rectangle:
    """This class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """__init__ method
        This method creates an instance of the class

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for <width> attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for <width> attribute

        Args:
            value (int): The width of the rectangle to be set

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Getter method for <height> attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for <height> attribute

        Args:
            value (int): The height of the rectangle to be set

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value
