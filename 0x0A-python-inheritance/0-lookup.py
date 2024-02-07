#!/usr/bin/python3
"""
 Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.
"""


def lookup(obj):
    """returns list of object's attribute and methods"""
    return dir(obj)
