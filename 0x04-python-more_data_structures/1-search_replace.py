#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """ Replaces all occurrences of an element by another in a new list """

    new_list = my_list.copy()
    for i in new_list:
        for j in i:
            if j == search:
                new_list[j] == replace

    return new_list
