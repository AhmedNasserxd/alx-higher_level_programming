#!/usr/bin/python3
"""
Module 2-is_same_class

Contains is_same_class
to check if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance
        of the specified class; otherwise False.
    """
    return type(obj) == a_class
