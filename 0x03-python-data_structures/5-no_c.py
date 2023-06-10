#!/usr/bin/python3
def no_c(my_string):
    copy_string = my_string
    for char in my_string:
        if char == 'C' or char == 'c':
            copy_string = copy_string.replace(char, '')
    return copy_string
