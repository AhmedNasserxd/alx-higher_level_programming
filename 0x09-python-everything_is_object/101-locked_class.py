#!/usr/bin/python3
"""To define locked class"""


class LockedClass:
    """
    LockedClass: A class that prevents the dynamic
        creation of new instance attributes, except for 'first_name'.
    """
    __slots__ = ("first_name",)
