#!/usr/bin/python3

""" NO module importation allowed
"""


def print_square(size):
    """ Function to print square of certain size
    """

    for i in range(size):
        if size is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is float:
            raise TypeError("size must be an integer")
        else:
            [print("#", end="") for j in range(size)]
            print()
