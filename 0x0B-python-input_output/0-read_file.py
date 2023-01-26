#!/usr/bin/python3
''' Contains a function that reads a file.
Usage:
    ./0-read_file.py
Author:
    Abdulsalam Abdulsomad .A. - January 26th, 2023.
'''


def read_file(filename=""):
    ''' A function that reads a text file (UTF8) and prints it to stdout
    Parameters:
        -----------
        filename(str) = Name of the file to read and print.
    '''

    with open(filename, 'r', encoding='utf-8') as myfile:
        print(myfile.read(), end='')
