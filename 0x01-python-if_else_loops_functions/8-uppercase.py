#!/usr/bin/python3

def uppercase(s):
    """Prints a string in uppercase followed by a new line."""
    """NEW BLANK"""

    for char in s:
        uppercase_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print("{}".format(uppercase_char), end="")
    print()


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
