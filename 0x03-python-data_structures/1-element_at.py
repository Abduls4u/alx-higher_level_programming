#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0:
        return (None)
    if idx > length:
        return (None)
    my_list[idx]