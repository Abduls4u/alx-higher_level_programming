#!/usr/bin/python3
def uniq_add(my_list=[]):
    for i in range(0, len(my_list)):
        if my_list[i] != my_list[i+1]:
            my_list[i] += my_list[i+1]
    return (a)
