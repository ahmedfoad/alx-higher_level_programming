#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniq_list = list(set(my_list))
    for item in uniq_list:
        result += item

    return (result)
