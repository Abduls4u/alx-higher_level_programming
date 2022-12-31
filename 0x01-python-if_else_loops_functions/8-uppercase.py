#!/usr/bin/python3
def islower(char):
    if ord(char) <= ord('z') and ord(char) >= ord('a'):
        return (True)
    else:
        return (False)


def uppercase(str):
    new = ""
    for a in str:
        if islower(a):
            new += chr(ord(a) - ord('a'))
        else:
            new += a
        print("{}".format(new), end="")
    print()
