#!/usr/bin/python3
''' A module that contains a function that adds 2 integers.
Usage:
    ./0-add_integer.py
Author:
    Abdulsalam Abdulsomad .A. - December 29th, 2022.
'''


def add_integer(a, b=98):
    ''' A function that returns the sum of two integers.
    parameters:
    ***********
        a(int): first argument.
        b(int): second argument.
    Return:
    *******
        type == int.
           The sum of the two integers passed as arguments.
    Raise:
    ******
        TypeError: if arguments are not ints.
    '''

    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
