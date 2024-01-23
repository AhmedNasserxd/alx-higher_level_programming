#!/usr/bin/python3
"""Python class for python bytecode"""


import math


class MagicClass:
    """Python class equivalent to the provided Python bytecode."""

    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass.

        Parameters:
        - radius (number): The radius of the MagicClass (default is 0).

        Raises:
        - TypeError: If radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Computes and returns the area of the MagicClass.

        Returns:
        float: The area of the MagicClass.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Computes and returns the circumference of the MagicClass.

        Returns:
        float: The circumference of the MagicClass.
        """
        return 2 * math.pi * self.__radius
