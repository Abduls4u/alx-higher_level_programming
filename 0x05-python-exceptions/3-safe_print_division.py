#!/usr/bin/python3
def safe_print_division(a, b):
    if b == 0:
        c = None
    else:
        c = a / b
    try:
        print("Inside result: {}".format(c))
    except:
        pass
    finally:
        print("{} / {} = {}".format(a, b, c))
