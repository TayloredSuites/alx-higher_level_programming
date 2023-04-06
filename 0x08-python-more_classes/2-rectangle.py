#!/usr/bin/python3

""" No module importation allowed """


class Rectangle:
    """ Class that defnes a rectangle based on 1-rectangle.py
    """

    def __init__(self, width=0, height=0):
        """ Initializes the instances of width and height
        Note:
            Private attributes are created
        Args:
            width (int): horizontal length of rectangle
            height (int): vertical length of rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """ A property to retrieve private instance of self
            """

            return self.__width

        @width.setter
        def width(self, value):
            """ Function to set the width of a rectangle
            Note:
                Retrieves prvate instance of width to set it to value
            """

            if type(width) is not int:
                raise TypeError('width must be an integer')
            elif width < 0:
                raise ValueError('width must be >= 0')
            else:
                self.__width = value

        @property
        def height(self):
            """ A property to retrieve private instance of self
            """

            return self.__height

        @height.setter
        def height(self, value):
            """ Function to set the height of a rectangle
            Note:
                Retrieves private instance of width to set it to value
            """

            if type(height) is not int:
                raise TypeError("height must be an integer")
            elif height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

        def area(elf):
            """ Class function to return current rectangle area
            """

            return self.width * self.height

        def perimeter(self):

            """ Class function to return current perimeter of rectangle
            """

            return (2 * self.width) + (2 * self.height)
