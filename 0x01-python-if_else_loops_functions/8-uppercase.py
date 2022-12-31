#!/usr/bin/python3
def is_lower(char):
    if ord(char) <= ord('z') and ord(char) >= ord('a'):
        return (True)
    else:
        return (False)


def uppercase(string):
    upper_string = ""
    for char in string:
        if is_lower(char):
            upper_char = chr(ord(char) - ord('a') + ord('A'))
            upper_string += upper_char
        else:
            upper_string += char
    print("{}".format(upper_string), end="")
    print()
