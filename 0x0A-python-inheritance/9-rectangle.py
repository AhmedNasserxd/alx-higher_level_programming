#!/usr/bin/python3
"""
Module 9-rectangle

Contains class BaseGeometry
representing a base geometry
and validates the value with integer_validation
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle that inherits from BaseGeometry.

    Methods:
        __init__(self, width, height):
        Initializes the rectangle with width and height.
        area(self): Computes the area of the rectangle.
        __str__: String representation of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes and validates the width and height of the rectangle.

        Args:
            width (int): The width of the rectangle (private).
            height (int): The height of the rectangle (private).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """to extend parent's empty method and returns area"""
        return self.__width * self.__height

    def __str__(self):
        """prints Rectangle width/height"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
