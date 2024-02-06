#!/usr/bin/python3
"""
Module to return the dictionary description
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Return the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representation of the object suitable
        for JSON serialization.
    """
    attributes = obj.__dict__
    return {key: value for key, value in attributes.items()
            if isinstance(value, (str, int, list, dict, bool))}


if __name__ == "__main__":
    class_to_json()
