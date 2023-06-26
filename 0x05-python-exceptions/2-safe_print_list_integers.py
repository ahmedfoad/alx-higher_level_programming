#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for item in my_list:
            print("{:d}".format(item), end="")
            x += 1
    except IndexError:
        pass
    print()
    return x
