#!/usr/bin/python3
''' A module that contains a class that inherits.
Usage:
    ./1-my_list.py
Author:
    Abdulsalam Abdulsomad .A. - January 20th, 2023.
'''


class MyList(list):
    '''Subclass'''
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        ''' Prints a sorted list'''
        print(sorted(self))
