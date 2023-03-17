#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """ Computes the square value of all integers of a matrix """

    for i in matrix:
        print(list(map(lambda x: x**2, i)))
