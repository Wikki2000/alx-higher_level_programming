#!/usr/bin/python3
"""Python class MagicClass that does Python bytecode"""
import math


class MagicClass:
    """MagicClass with similar functionality as the provided bytecode."""

    def __init__(self, radius=0):
        """Constructor for MagicClass.

        Args:
            radius (int or float): Radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number.
        """
        if type(radius) not in [int, float]:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius
