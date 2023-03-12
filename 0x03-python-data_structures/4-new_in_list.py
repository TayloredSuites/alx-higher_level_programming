#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """ Replace list element at position without modifying original """

    if idx < 0:
        return my_list

    elif idx >= len(my_list):
        return my_list
    else:
        list_copy = my_list.copy()
        list_copy[idx] = element
        return list_copy
