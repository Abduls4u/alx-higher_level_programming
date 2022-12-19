#!/usr/bin/pytjon3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print("{}".format(a[i]), end="")
        except IndexError:
            print("{}".format(a[i-1]))
    return (i)
