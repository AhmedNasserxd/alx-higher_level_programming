#!/usr/bin/python3
"""
Module to read and print the contents of a text file to stdout.
"""


def read_file(filename=""):
    """
    Read the contents of a text file and print to stdout.

    Args:
        filename (str): The name of the text file to read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')


if __name__ == "__main__":
    read_file()
