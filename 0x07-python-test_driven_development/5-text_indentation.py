#!/usr/bin/python3
''' A module that contains a function that prints a text with 2 new lines after specific characters
Usage:
    ./5-text_indentation.py
Author:
    Abdulsalam Abdulsomad .A. - December 31st, 2022.
'''


def text_indentation(text):
    ''' A function that prints a text with 2 new lines after each of these characters: ., ? and :
    parameters:
    ***********
        text(str): text to be printed.
    Return:
    *******
        type == void.
    Raise:
    ******
        TypeError: if text is not a string.
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    for i in text:
        if i in ['.', '?', ':']:
            new_text += i + '\n' + '\n'
        else:
            new_text += i
    print(new_text)
