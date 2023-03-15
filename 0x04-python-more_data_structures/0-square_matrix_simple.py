#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """ Computes the square value of all integers of a matrix """
    matrix_copy = matrix.copy()

    for i in matrix:
        list(map(lambda i: i**2, matrix_copy))
