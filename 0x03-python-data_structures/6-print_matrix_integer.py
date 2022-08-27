#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if len(matrix[0]) != 0:
        rows = len(matrix)
        columns = len(matrix[0])

        for i in range(rows):
            for j in range(columns):
                if j == columns - 1:
                    print("{:d}".format(matrix[i][j]))
                else:
                    print("{:d}".format(matrix[i][j]), end=" ")
    else:
        print()
