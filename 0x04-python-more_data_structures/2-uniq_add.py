#!/usr/bin/python3

def uniq_add(my_list=[]):
    """ adds all unique integers in a list (only once for each integer). """

    set_unique = set(my_list)
    return (set(map(lambda x: sum(x), set_unique)))
