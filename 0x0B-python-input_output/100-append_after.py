#!/usr/bin/python3
""" Module to execute function that appends a line"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append a line of text to a file
    after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to append
        after each line containing the search_string.

    Returns:
        None
    """
    with open(filename, mode="r+", encoding="utf-8") as f:
        new_text = ""
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
        f.seek(0)
        f.write(new_text)
