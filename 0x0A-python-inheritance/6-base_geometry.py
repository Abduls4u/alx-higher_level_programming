#!/usr/bin/python3
''' A module that contains the class BaseGeometry.
Usage:
    ./6-base_geometry.py
Author:
    Abdulsalam Abdulsomad .A. - January 22nd, 2023.
'''


class BaseGeometry:
    ''' Class BaseGeometry. '''

    def __init__(self, width=0, height=0):
        '''Constructs all the necessary attributes for the class. '''
        pass

    def area(self):
	    raise Exception('area() is not implemented')
