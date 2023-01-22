#!/usr/bin/python3
''' A module that contains the class BaseGeometry.
Usage:
    ./7-base_geometry.py
Author:
    Abdulsalam Abdulsomad .A. - January 22nd, 2023.
'''


class BaseGeometry:
    ''' Class BaseGeometry. '''

    def __init__(self):
        '''Constructs all the necessary attributes for the class. '''
        pass

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
