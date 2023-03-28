#!/usr/bin/python3

""" No module importation allowed
"""


class Square:
    """ Defines a square based on 2-square.py
    """

    def __init__(self, size=0):
        """ Initializes the instance of size

        Note:
            Private attribute is created

        Args:
            size : square size
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Class fuction to return current square area
        """

        return self.__size * self.__size
