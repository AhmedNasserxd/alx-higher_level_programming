#!/usr/bin/python3

def uppercase(s):
"""Prints a string in uppercase followed by a new line."""
for char in s:
uppercase_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
print("{}".format(uppercase_char), end="")
print()

if __name__ == "__main__":
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")