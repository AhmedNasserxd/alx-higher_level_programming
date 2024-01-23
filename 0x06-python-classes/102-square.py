#!/usr/bin/python3
"""Square class definition3x7"""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (number): The size of the square (default is 0).

        Raises:
        - TypeError: If size is not a number.
        - ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
        number: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator for Square instances based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparator for Square instances based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparator for Square instances based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparator for Square instances"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparator for Square instances based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparator for Square instances"""
        return self.area() >= other.area()
