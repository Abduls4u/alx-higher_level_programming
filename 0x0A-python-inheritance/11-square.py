#!/usr/bin/python3
''' A module that contains the class square that inherits from class Rectangle.
Usage:
    ./11-square.py
Author:
    Abdulsalam Abdulsomad .A. - January 22nd, 2023.
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' A class Square that inherits from Rectangle (9-rectangle.
py). (task based on 10-square.py).'''

    def __init__(self, size):
        '''Constructs all the necessary attributes for the class.
        parameters:
        ___________
             size: length of the square
        '''

        self.__size = size
        self.integer_validator('size', size)
        super().__init__(size, size)

    def area(self):
        ''' returns the square of size. '''

        return (self.__size ** 2)
