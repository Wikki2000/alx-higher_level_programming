#!/usr/bin/python3
"""Rectangle Module: This class models a Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherited from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method
        This is a constructor of a class instance

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
            x (int): The x-coordinate of the Rectangle (default is 0)
            y (int): The y-coordinate of the Rectangle (default is 0)
            id (int): The identifier of the Rectangle (default is None)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """Getter method for <width> attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter method for <width> attribute"""
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    @property
    def height(self):
        """Getter method for <height> attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter method for <height> attribute"""
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    @property
    def x(self):
        """Getter method for <x> attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter method for <x> attribute"""
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def y(self):
        """Getter method for <y> attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter method for <y> attribute"""
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """ calculate rectangle area """
        return self.width * self.height

    def display(self):
        """ Display Rectangle as a str rep suing '#' char """
        for item in ['#' * self.__width] * self.__height:
            print(item)

    def __str__(self):
        """ String rep. of the instances """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the attribute of the rectangle class"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        # To prevent out of range error
        for i in range(min(len(args), len(attributes))):
            setattr(self, attributes[i], args[i])

        # Update attribute using Non-keyword arguement
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Return dict. of an object""""
        obj_dict = self.__dict__.copy()
        return obj_dict
