#!/usr/bin/python3
''' A class that defines a square.
Usage:
    ./1-rectangle.py
Author:
    Abdulsalam Abdulsomad .A. - January 2nd, 2023.
'''


class Rectangle:
    ''' A class that represents a square.'''

    def __init__(self, width=0, height=0):
        '''Constructs all the necessary attributes for the rectangle object.
        parameters:
        ___________
             width: Breadth of the rectangle.
             height: Length of the rectangle.
        '''

        self.width = width
        self.height = height

    @property
    def width(self):
        '''Getter method to retrieve width.'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''setter method to set the value of width.'''
        if not type(value) is int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getter method to retrieve the heght.'''
        return(self.__height)

    @height.setter
    def height(self, value):
        '''setter method to set value of height.'''
        if not type(value) is int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' returns the area of a rectangle.
        parameters:
        __________
        Return:
            width X height.
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        ''' returns the perimeter of a rectangle.
        parameters:
        __________
        Return:
            2(width + height).
        '''
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self) -> str:
        '''prints the rectangle in an informal and printablr representation'''
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for length in range(self.__height):
            for breadth in range(self.__width):
                rectangle += '#'
            if length < (self.__height - 1):
                rectangle += "\n"
        return (rectangle)
