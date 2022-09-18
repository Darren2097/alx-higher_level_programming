#!/usr/bin/python3
"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """matrix_divided function"""

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            if len(matrix[i]) != c:
                raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[0 for i in range(c)] for j in range(r)]

    for i in range(r):
        for j in range(c):
            new = matrix[i][j]
            if not isinstance(new, int) and not isinstance(new, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                new_matrix[i][j] = float("%0.2f" % (new / div))

    return new_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
