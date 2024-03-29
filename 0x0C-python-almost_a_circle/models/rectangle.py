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
             x: x axis
             y: y axis
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
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''A getter mwtjod to retrieve y '''
        return (self.__y)

    @y.setter
    def y(self, value):
        ''' A setter method to set value of y'''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' Returns the area value of the Rectangle instance '''
        return (self.__width * self.__height)

    def display(self):
        ''' prints in stdout the Rectangle instance with the character #'''
        for y in range(self.__y):
            print('')
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')
            print('#' * self.__width)

    def __str__(self):
        '''returns an informal representation'''
        rect = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)
        return (rect)

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if len(args) != 0:
            count = 0
            for argument in args:
                if count == 0:
                    if argument is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = argument
                if count == 1:
                    self.__width = argument
                if count == 2:
                    self.__height = argument
                if count == 3:
                    self.__x = argument
                if count == 4:
                    self.__y = argument
                count += 1
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        ''' return dictionary representation of a Rrctangle'''
        return {
               "id": self.id,
               "width": self.__width,
               "height": self.__height,
               "x": self.__x,
               "y": self.__y
            }
