#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    sq = lambda x: x ** 2
    new_matrix = [list(map(sq, row)) for row in new_matrix]
    return new_matrix
