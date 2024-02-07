#!/usr/bin/python3

"""Module 100-my_int"""


class MyInt(int):
    """Subclass of int with inverted == and != operators"""

    def __eq__(self, other):
        """Inverts the == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the != operator"""
        return super().__eq__(other)
