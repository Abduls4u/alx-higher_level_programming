#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x == 0:
        return (0)
    else:
        try:
            for i in range(x):
                print("{}".format(a[i]), end="")
            return (x)
        except IndexError:
            for i in my_list:
                print("{}".format(i), end="")
            return(i)
