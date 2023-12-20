#!/usr/bin/python3

"""Square module: This <square> module models a sqaure class"""


class Square:
    """Class definition of a square"""

    def __init__(self, size=0):
        """__init__ method
        This create an instance of a class

        Args:
            size (int): The <size> attribute of a square
        """
        self.__size = size

    @property
    def size(sef):
        """Getter method of <size> attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method of size attribute

        Args:
            Value (int): The size of the square class

        Raises:
            TypeError: If size not an integer
            ValueError: If size less than 0
        """
        self.__size = value

    def area(self):
        """Area method: Calculate area of a square

        Return:
            int: Return the square of the size
        """
        return self.__size ** 2

    def my_print(self):
        """my_print method: Print the square using '#' character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end=" ")
                print()
