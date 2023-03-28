#!/usr/bin/python3

""" Module creates a private attribute size """

class Square:
    """ Defines a square based on 0-square.py
    and initializes it to size

    """

    def __init__(self, size):
        """ Initializes the instance of size

        Note:
            Private attribute is created

        Args:
            size : square size
        """
        self.__size = size
