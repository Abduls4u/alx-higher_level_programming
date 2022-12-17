#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = [[row[i] ** 2 for i in range(len(row))] for i in matrix]
    return (mat)
