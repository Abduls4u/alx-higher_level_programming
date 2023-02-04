#!/usr/bin/python3
''' A module that inherits from Base.
Usage:
    ./rectangle.py
Author:
    Abdulsalam Abdulsomad .A. - February 4th, 2023.
'''
from models.base import Base


class Rectangle(Base):
    ''' A class that represents a rectangle.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Constructs all the necessary attributes for the rectangle object.
        parameters:
        ___________
             width: Breadth of the rectangle.
             height: Length of the rectangle.
        '''

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Getter method to retrieve width.'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''setter method to set the value of width.'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Getter method to retrieve the heght.'''
        return(self.__height)

    @height.setter
    def height(self, value):
        '''setter method to set value of height.'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        ''' Getter method to retrieve value of x'''
        return (self.__x)

    @x.setter
    def x(self, value):
        '''setter metjod to set value of height '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''A get5er mwtjod to retrieve y '''
        return (self.__y)

    @y.setter
    def y(self, value):
        ''' A setter method to set value of y'''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value
