#!/usr/bin/python3
''' A module that contains a function that tests if an object is
a subclass.
Usage:
    ./4-inherits_from.py
Author:
    Abdulsalam Abdulsomad .A. - January 22nd, 2023.
'''


def inherits_from(obj, a_class):
    ''' returns True if the object is an an instance of a class
that inherited (directly or indirectly) from the specified class
;otherwise False
    parameters:
    -----------
        obj: object to test.
        a_class: class to be specified.
    '''

    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return (True)
    else:
        return (False)
