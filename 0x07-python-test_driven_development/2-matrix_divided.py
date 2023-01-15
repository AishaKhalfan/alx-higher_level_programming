#
/usr/bin/python3
"""
This is the 2-matrix_divided module.
The 2-matrix_divided module supplies one function,matrix_divided()
"""


def matrix_divided(matrix, div):
    """
    Return the division of matrix and div.
    Args:
        matrix (list(list)): the first value
        div (int or float): the second value
    """
    mtrx_type_E = 'matrix must be a matrix (list of lists) of integers/floats'
    mtrx_lenError = 'Each row of the mmatrix must have the same size'
    div_typError = 'div must be a number'
    div_zeroError = 'division by zero'

    row_len = 0
    if type(matrix) is not list:
        raise TypeError(mtrx_type_E)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(mtrx_type_E)
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(mtrx_type_E)
        if len(row) is not row_len and row_len is not 0:
            raise TypeError(mtrx_lenError)
        row_len = len(row)

    if type(div) is not in [int, float]:
        raise TypeError(div_typError)
    if div is 0:
        raise ZeroDivisionError(div_zeroError)

    return [[round(nb / div, 2) for nb in row] for row in matrix]
