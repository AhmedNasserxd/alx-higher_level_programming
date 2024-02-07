#!/usr/bin/python3
"""
Module 8-rectangle

Contains class BaseGeometry
representing a base geometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a base geometry."""

    def __init__(self, width, height):
        """The instantiation of a rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
