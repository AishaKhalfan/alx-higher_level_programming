#!/usr/bin/python3

from math import factorial


def pascal_triangle(n):
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
