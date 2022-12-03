#!/usr/bin/python3
def uppercase(str):
    if str == 'a' or str <= 'z':
        for str in range(ord('a'), ord('z')):
            str = ord(str)
            str = str-32
            str = chr(str)
            print('{}'.format(str))
    else:
        print("{}".format(str))
