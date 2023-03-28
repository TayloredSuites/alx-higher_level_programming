#!/usr/bin/python3

""" No module import allowed
"""

class Square:
    """ Defines a square of known or unknown size
    """
    def __init__(self, size=0):
        """ Intializes the instance of size

        Note:
            Private attribute of __init__ is created

        Args:
            size (int): the size of square getter value
        """
        if size < 0:
            raise ValueError('size must be >= 0')
        elif type(size) is not in:
            raise TypeError('size must be an integer')
        else:
            self.__size = size
