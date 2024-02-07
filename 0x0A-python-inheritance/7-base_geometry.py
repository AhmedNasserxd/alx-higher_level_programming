#!/usr/bin/python3
"""
Module 7-base_geometry

Contains class BaseGeometry
that computes the area of the geometry
and validates through the value integer_validator
"""


class BaseGeometry:
    """
    A class representing a base geometry.
    """

    def area(self):
        """
        Computes the area of the geometry.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to ensure it's an integer and greater than 0.

        Args:
            name: A string representing the name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
