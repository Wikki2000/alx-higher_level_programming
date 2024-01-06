#!/usr/bin/python3

"""Rectangle module: This class model a rectangle"""


class Rectangle:
    """Class definition of a rectangle"""

    def __init__(self, width=0, height=0):
        """__init__ method
        This method creates an instance of the class

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    """create a property method for private instance"""
    @property
    def width(self):
        return self.__width

    """retrieve the property instance"""
    @width.setter
    def width(self, value):
        """Setter method for <width> attribute

        Args:
            value (int): The width of the rectangle to be set

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
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
        """Setter method for <width> attribute

        Args:
            value (int): The width of the rectangle to be set

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This method calculate the area of a square"""
        return self.__height * self.__width

    def perimeter(self):
        """This method calculate the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """This method print the sqaure as str using '#' character"""
        if self.__height == 0 or self.__width == 0:
            return ""
        return '\n'.join(['#' * self.__width] * self.__height)

        def __repr__(self):
        """ return a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
