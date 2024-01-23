#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Class that defines a square."""

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square.

        Note:
        The size is a private attribute, denoted by the double underscore.
        """
        self.__size = size
