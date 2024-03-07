#!/usr/bin/python3

"""
Generate a  Pascal’s triangle of n number of rows
"""


def pascal_triangle(n):
    """
    Generate a  Pascal’s triangle of n number of rows

    Args:
        n(int): number of rows

    Returns:
        list of lists of integers representing the Pascal’s triangle
    """

    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            prev_row = triangle[-1]
            row.extend([prev_row[j] + prev_row[j+1]
                        for j in range(len(prev_row)-1)])
            row.append(1)
        triangle.append(row)

    return triangle
