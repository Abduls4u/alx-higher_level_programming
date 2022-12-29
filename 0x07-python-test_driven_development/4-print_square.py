#!/usr/bin/python3
''' A module that contains a function that prints a square with #.
Usage:
    ./4-print_square.py
Author:
    Abdulsalam Abdulsomad .A. - December 29th, 2022.
'''


def print_square(size):
    ''' A function that prints a square with length == size.
    parameters:
    ***********
        size(int): length of the square.
    Return:
    *******
        type == void.
    Raise:
    ******
        TypeError: if size is not an int.
        valueError: if size is less than 0.
        TypeError: if size is a float and is less than 0.
    '''

    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (isinstance(size, float) and (isinstance(size, float) < 0)):
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
