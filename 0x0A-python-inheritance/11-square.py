#!/usr/bin/python3
"""
Module 11-square

Contains class BaseGeometry
with public instance method area and integer_validation

Contains subclass Rectangle with instantiation of private attributes
width and height, validated by parent,
extends parent's area method and prints with __str__

Contains subclass Square with instantiation of private attribute size,
validated by superclass,
and prints with __str__
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square that inherits from Rectangle,
    which inherits from BaseGeometry.

    Methods:
        __init__(self, size): Initializes the square with a size.
        __str__(self): String representation of the square.
    """
    def __init__(self, size):
        """
        Initializes the square with the given size.

        Args:
            size (int): The size of the square (private).
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """prints [Rectangle] <width>/<height>"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
