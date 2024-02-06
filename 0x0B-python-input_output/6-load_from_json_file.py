#!/usr/bin/python3
"""
Module to create an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python data structure represented by the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == "__main__":
    load_from_json_file()
