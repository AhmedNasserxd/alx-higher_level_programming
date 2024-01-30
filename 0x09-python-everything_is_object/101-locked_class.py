#!/usr/bin/python3

"""
LockedClass: A class that prevents the dynamic
    creation of new instance attributes, except for 'first_name'.
"""


class LockedClass:
    __slots__ = ("first_name",)

    def __init__(self):
        """
        Initializes an instance of LockedClass.
        """
        pass
