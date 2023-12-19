#!/usr/bin/python3


"""This module define a <square> call"""

class Square:
    """A definition of a class <square>"""

    def __init__(self, size=0):
        """__init__ method
        This method creates a private instance of a square class

        Args:
            size (int): Size of the square set to 0 by default

        Raises:
            TypeError: If size is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Area of a square
        This method calculates the area of a square

        Args:
            No Args

        Returns:
            The area of the square
        """
        return self.__size ** 2
