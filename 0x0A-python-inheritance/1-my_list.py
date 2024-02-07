#!/usr/bin/python3
"""
Module 1-my_list

Contains MyList
class of list that provides additional functionality;
Prints the list sorted in ascending order
"""


class MyList(list):
    """inherits from list

    methods:
    print_sorted(self)
    """
    def print_sorted(self):
        """prints list of ints all sorted in ascending order"""
        print(sorted(self))
