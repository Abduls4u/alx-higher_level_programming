#!/usr/bin/python3
''' A class that defines a rectangle.
Usage:
    ./2-rectangle.py
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

    def __str__(self):
        '''returns unofficial representation'''
        rect = ''
        if self.width == 0 or self.__height == 0:
            rect = ''
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rect += '#'
                    if j == self.__width - 1 and i != self.__height - 1:
                        rect += '\n'
        return (rect)

    def __repr__(self):
        '''returns the official representation'''
        rect = f"Rectangle({self.__width}, {self.__height})"
        return (rect)
