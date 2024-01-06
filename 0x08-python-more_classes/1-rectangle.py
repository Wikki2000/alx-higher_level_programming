#!/usr/bin/python3

"""Rectangle module: This class models a Rectangle"""


class Rectangle:
    """This class define a rectangle"""

    def __init__(self, width=0, height=0):
        """__init__ method
        This method create an instance of the class

        Args:
            width (int): The width of rectangle
            height (int): The height of rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter method for <width> attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for <width> attribute

        Args:
            Value (int): The width of rectangle to be set

        Raise:
            TypeError: If width not integer
            ValueError: If width < 0
        """

        if width < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value
        
    @property
    def height(self):
        """Getter method for <height> attribute"""
        return self.__height
    
    @width.setter
    def height(self, value):
        """Setter method for <height> attribute

        Args:
            Value (int): The height of rectangle to be set

        Raise:
            TypeError: If height not integer
            ValueError: If height < 0
        """

        if height < 0:
            raise ValueError("height must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value
