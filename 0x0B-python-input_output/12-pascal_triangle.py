#!/usr/bin/python3
"""Creates a function that returns a list of lists of integers representing
the Pascal’s triangle of n"""


def pascal_triangle(n):
    """pascal_triangle method"""

    triangle = []

    if n <= 0:
        return triangle
    else:
        for r in range(n):
            if r == 0:
                triangle.append([1])
            elif r == 1:
                triangle.append([1, 1])
            else:
                triangle.append([1 for i in range(r + 1)])
                for c in range(1, len(triangle[r]) - 1):
                    triangle[r][c] = triangle[r - 1][c - 1] + triangle[r-1][c]

    return triangle

if __name__ == '__main__':
    def print_triangle(triangle):
        """Print the triangle"""
                         
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(8))
