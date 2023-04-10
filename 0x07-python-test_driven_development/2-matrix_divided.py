#!/usr/bin/python3

""" No module importation allowed
"""


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix

    Note:
        matrix must be a list of lists of integers or floats, otherwise
        raise a TypeError exception with the message matrix must be a
        matrix (list of lists) of integers/floats

        Each row of the matrix must be of the same size, otherwise
        raise a TypeError exception with the message Each row of the matrix
        must have the same size

        div must be a number (integer or float), otherwise raise a TypeError
        exception with the message div must be a number

        div can’t be equal to 0, otherwise raise a ZeroDivisionError
        exception with the message division by zero

        All elements of the matrix should be divided by div,
        rounded to 2 decimal places

        Returns a new matrix

    Args:
        matrix (list): a list of integers or floars
        div (int/float): the denominator to each matrix element

    Return:
        matrix elements after division to 2 decimal places
    """

    for i in matrix:
        if type(i) != list and type(i) != float:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if type(i) != list and type(i) != int:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(i) != len(i):
            raise TypeError('Each row of the matrix must have the same size')
            for j in i:
                if type(j) != int & type(j) != float:
                    raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        
            else:
                if type(div) != int & type(div) != float:
                    raise TypeError('div must be a number')
                    if div == 0:
                        raise TypeError('division by zero')
                        
                    else:
                        return round(list(map(lambda x: x / 2, i)))
