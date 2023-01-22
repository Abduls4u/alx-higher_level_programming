#!/usr/bin/python3
''' A module that contains the classRecyangle that inherits from BaseGeometry.
Usage:
    ./8-rectangle.py
Author:
    Abdulsalam Abdulsomad .A. - January 22nd, 2023.
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' A  class Rectangle that inherits from BaseGeometry.'''

    def __init__(self, width, height):
        '''Constructs all the necessary attributes for the class.
        parameters:
        ___________
             width: Breadth of the rectangle.
             height: Length of the rectangle.
        '''

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator('height', height)
