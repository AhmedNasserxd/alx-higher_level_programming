#!/usr/bin/python3
"""
Module 3-is_kind_of_class

Contains is_kind_of_class
to Check if the object is an instance of, or if the object is an instance
of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
