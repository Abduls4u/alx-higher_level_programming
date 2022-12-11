#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_list[idx] = element
    rep = my_list[idx]
    if idx < 0 or idx >= (len(my_list)):
        return (my_list)
    else:
        return (rep)
