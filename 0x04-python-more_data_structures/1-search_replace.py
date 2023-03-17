#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """ Replaces all occurrences of an element by another in a new list """

    new_list = my_list.copy()
    for i in new_list:
        if i == search:
            new_list[i] == replace

    return new_list
