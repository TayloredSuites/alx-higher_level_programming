#!/usr/bin/python3

""" No module imports allowed
"""


class Square:
    """ Defines a square by 3-square.py
    """

    def __init__(self, size=0):
        """ Initializes the instance of size

        Note:
            Private attribute of size is created

        Args:
            size : square size of no type/validation
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Class funtion to return current square area
        """

        return self.__size * self.__size


    @property
    def size(self):
        """ A property ot retrieve private instance of self
        """

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
