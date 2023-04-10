#!/usr/bin/python3

""" No module import allowed
"""


def add_integer(a, b=98):
    """ A function that adds two integers

    Note:
        a and b must be first casted to integers if they are float
        a and b must be integers or floats, otherwise raise a TypeError
        exception with the message a must be an integer or b must be an integer

    Args:
        a (int): one of the two integers to the added
        b (int): the other of the two integers local scope of 89

    Return: sum of two ints a and b
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
