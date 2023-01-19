#!/usr/bin/python3
# 14-pascal_triangle.py
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Returns Pascals Triangle of size n"""
    if n <= 0:
        return []

    # create an empty list to store the triangle
    t = []
    # loop through each row
    for i in range(n):
        t.append([])
        t[i].append(1)
        for j in range(1, i):
            t[i].append(t[i-1][j-1]+t[i-1][j])
        if i != 0:
            t[i].append(1)
    return t
