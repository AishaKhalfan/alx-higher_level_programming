#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])
    for n in range(matrix_rows):
        for m in range(matrix_columns):
            print(matrix[n][m] **2)
        print()
