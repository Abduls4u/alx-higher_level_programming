#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
        return (i)
    except IndexError:
        for i in my_list:
            if type(i) is int:
                print("{:d}".format(i), end="")
        return (i)
