#!/usr/bin/python3

def max_integer(my_list=[]):
    """ Finds the biggest integer of a list """

    biggest_int = my_list[0]

    if not my_list:
        return None
    else:
        for i in my_list:
            if i > biggest_int:
                biggest_int = i

    return biggest_int
