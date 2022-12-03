#!/usr/bin/python3
def uppercase(str):
    if str == range('a', 'z'):
        for str in range('a', 'z'):
            str = ord(str)
	    str = str-32
	    str = chr(str)
	    print('{}'.format(str))
    else:
        print("{}".format(str))
