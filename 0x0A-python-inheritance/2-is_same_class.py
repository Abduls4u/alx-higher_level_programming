#!/usr/bin/python3
''' A module that contains a function that tests if an object
is exactly an instance of the specified class.
Usage:
    ./2-is_same_class.py
Author:
    Abdulsalam Abdulsomad .A. - January 22nd, 2023.
'''


def is_same_class(obj, a_class):
    ''' returns True if the object is exactly ae instance of the
specified class ; otherwise False.
    parameters:
    -----------
        obj: object to test.
        a_class: class to be specified.
    '''

    if type(obj) is a_class:
        return (True)
    return (False)
