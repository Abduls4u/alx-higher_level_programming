#!/usr/bin/python3
''' Contains a function that appends to the end of a file.
Usage:
    ./2-append_write.py
Author:
    Abdulsalam Abdulsomad .A. - January 26th, 2023.
'''


def append_write(filename="", text=""):
    ''' A function that appends a string at the end of a text fil
e(UTF8) and returns the number of characters added
    Parameters:
    -----------
        filename(str): Name of the file to write to.
        text(str): text to be appended
    Return(int):
    ------------
        Number of chars written
    '''

    with open(filename, 'a', encoding='utf-8') as myfile:
        return (myfile.write(text))
