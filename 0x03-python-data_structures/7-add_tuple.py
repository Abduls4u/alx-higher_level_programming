#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1 or len(tuple_b) == 1:
        tuple_a[1] = 0
        tuple_b[1] = 0
    elif len(tuple_a) < 1 or len(tuple_b) < 1:
        tuple_a[0] = 0
        tuple_b[0] = 0
        tuple_a[1] = 0
        tuple_b[1] = 0

    add_1 = tuple_a[0] + tuple_b[0]
    add_2 = tuple_a[1] + tuple_b[1]
    total = (add_1, add_2)
    return (total)
