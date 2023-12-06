#!/usr/bin/python3
def sq(x):
    return x ** 2


def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    new_matrix = [list(map(sq, row)) for row in new_matrix]
    return new_matrix


"""
Another method to use is:
def square_matrix_simple(matrix=[]):
    return [[x**2 for x in row] for row in matrix]
"""
