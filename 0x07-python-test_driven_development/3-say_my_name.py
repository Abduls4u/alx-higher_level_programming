#!/usr/bin/python3
''' A module that contains a function that prints a \
    person's first and last name.
Usage:
    ./3-say_my_name.py
Author:
    Abdulsalam Abdulsomad .A. - December 29th, 2022.
'''


def say_my_name(first_name, last_name=""):
    ''' A function that prints My name is <first name> <last name>.
    parameters:
    ***********
        first_name(string): first argument.
        last_name(string): second argument.
    Return:
    *******
        type == void.
    Raise:
    ******
        TypeError: if arguments are not strings.
    '''
    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
