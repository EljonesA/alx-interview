#!/usr/bin/python3


def pascal_triangle(n):
    '''
    This function creates a pascal traingle of size n
    :param: n - triangle size
    '''
    # return empty list
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]  # start each row wtih a 1
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        if i > 0:
            row.append(1)  # end each row with a 1
        triangle.append(row)

    return triangle
