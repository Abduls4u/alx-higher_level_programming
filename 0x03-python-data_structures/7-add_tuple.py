#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1 or len(tuple_b) == 1:
        tup1 = list(tuple_a)
        tup2 = list(tuple_b)
        tup1.append('0')
        tup2.append('0')
        tuple_a = tuple(tup1)
        tuple_b = tuple(tup2)
    elif len(tuple_a) < 1 or len(tuple_b) < 1:
        tup1 = list(tuple_a)
        tup2 = list(tuple_b)
        tup1.append('0')
        tup2.append('0')
        tup1.append('0')
        tup2.append('0')
        tuple_a = tuple(tup1)
        tuple_b = tuple(tup2)

    add_1 = int(tuple_a[0]) + int(tuple_b[0])
    add_2 = int(tuple_a[1]) + int(tuple_b[1])
    total = (add_1, add_2)
    return (total)
