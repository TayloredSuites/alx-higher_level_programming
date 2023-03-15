#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """ Computes the square value of all integers of a matrix """
    matrix_copy = matrix.copy()

    for i in matrix:
        return list(map(lambda x: x**2, i))
