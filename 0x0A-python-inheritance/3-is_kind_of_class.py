#!/usr/bin/python3
''' A module that contains a function that tests if an object is
an instance of a class or its base class.
Usage:
    ./3-is_kind_of_class.py
Author:
    Abdulsalam Abdulsomad .A. - January 22nd, 2023.
'''


def is_kind_of_class(obj, a_class):
    ''' returns True if the object is exactly an instance of the
specified class or if the object is an instance of a clase
that inherited from, the specified class ; otherwise False.
    parameters:
    -----------
        obj: object to test.
        a_class: class to be specified.
    '''

    return (isinstance(obj, a_class))
