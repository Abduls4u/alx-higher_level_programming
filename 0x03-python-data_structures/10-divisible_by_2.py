#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return ()
    listcpy = []
    for i in my_list:
        listcpy.append(i % 2 == 0)
    return (listcpy)
