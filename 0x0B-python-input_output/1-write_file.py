#!/usr/bin/python3
''' Contains a function that writes to a file.
Usage:
    ./1-write_file.py
Author:
    Abdulsalam Abdulsomad .A. - January 26th, 2023.
'''


def write_file(filename="", text=""):
    ''' A function that writes a string to a text file (UTF8) and returns the number of characters written
    Parameters:
        -----------
        filename(str): Name of the file to write to.
        text(str): text to be written
    '''

    with open(filename, 'w', encoding='utf-8') as myfile:
        return (myfile.write(text))
