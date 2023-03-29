#!/usr/bin/python3

""" No module imports allowed
"""


class Square:
    """ Defines a square by 4-square.py
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
        """ Class function to return current square area
        """

        return self.__size * self.__size

    @property
    def size(self):
        """ A property ot retrieve private instance of self
        """

        return self.__size

    @size.setter
    def size(self, value):
        """ Property setter to set the value of the square size
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Prints to stdout the square with chatacter '#'
        """

        if size == 0:
            print()
        else:
            for i in range(self.__size):
                [print'#', end="") for j in range(self.__size)]
                print()
