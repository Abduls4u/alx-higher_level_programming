#!/usr/bin/python3
''' A class that defines a square.
Usage:
    ./0-square.py
Author:
    Abdulsalam Abdulsomad .A. - December 20th, 2022.
'''


class Square:
    ''' A class that represents a square.'''

    def __init__(self, size):
        '''Contains all the necessary attributes for the square object.
        parameters:
        ___________
             size(int): size of a square.
        '''

        self.__size = size
