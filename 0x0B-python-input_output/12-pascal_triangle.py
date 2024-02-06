#!/usr/bin/python3
"""
Module to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle of size n.

    Args:
        n (int): Size of the Pascal's triangle.

    Returns:
        list: List of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    pass
