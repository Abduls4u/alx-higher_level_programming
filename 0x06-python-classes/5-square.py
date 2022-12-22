#!/usr/bin/python3
''' A class that defines a square.
Usage:
    ./0-square.py
Author:
    Abdulsalam Abdulsomad .A. - December 20th, 2022.
'''


class Square:
    ''' A class that represents a square.'''

    def __init__(self, size=0):
        '''Constructs all the necessary attributes for the square object.
        parameters:
        ___________
            size(int): size of a square.
        '''

        self.__size = size
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        '''Getter method to retrieve '''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''setter method to set value.'''
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        ''' returns the area of a square.
        parameters:
        __________
        Return:
            square of size.
        '''
        return (self.__size ** 2)

    def my_print(self):
        '''Prints a square to stdout'''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print()
