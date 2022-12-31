#!/usr/bin/python3
def islower(char):
    if ord(char) <= ord('z') and ord(char) >= ord('a'):
        return (True)
    else:
        return (False)


def uppercase(str):
    new = ""
    for a in str:
        if islower(str):
            new += chr(ord(str) - ord('a'))
        else:
            new += str
        print("{}".format(new), end="")
    print()
