#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return ()
    length = len(matrix)
    for i in range(length):
        for j in range(len(matrix[i])):
            end =" "
            if (j + 1) == len(matrix[i]):
                end = ""
            print("{:d}".format(matrix[i][j]), end=end)
    print()
