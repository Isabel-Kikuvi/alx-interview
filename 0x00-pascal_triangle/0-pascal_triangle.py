#!/usr/bin/python3
"""Module contains pascal_triangle"""


def pascal_triangle(n):
    """Reps Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        t = triangles[-1]
        temp = [1]
        for i in range(len(t) - 1):
            temp.append(t[i] + t[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
