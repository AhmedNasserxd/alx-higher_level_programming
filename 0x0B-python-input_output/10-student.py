#!/usr/bin/python3
"""
Module defining a Student class.
"""


class Student:
    """
    A class to represent a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with a first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings representing attributes to retrieve
            Default is None.

        Returns:
            dict: A dictionary containing the specified
            attributes of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}


if __name__ == "__main__":
    Student()
