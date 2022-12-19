#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as ex:
        sys.stderr.write("Exception: " + ex.__str__())
        return(False)
    else:
        return (True)
    print()
