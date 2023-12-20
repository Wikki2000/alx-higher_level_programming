#!/usr/bin/python3

"""Square module: This class nodels a square"""


class Square:
    """This class defines a square"""

    def __init__(self, size=0):
        """__init__ method
        This method create an instance of class

        Args:
            size (int): The size of a square set to 0 by default

        Raises:
            TypeError: If size not an integer
            ValueError: If size < 0
        """
        self.__size = size

    @property
    def size(self):
        """Getter method for <size> attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for <size> attribute

        Args:
            value (int): The size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Area method

        Return:
            int: The area of a square
        """
        return self.__size ** 2
