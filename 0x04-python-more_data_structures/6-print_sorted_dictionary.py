#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """ Function that prints a dictionary by ordered keys """

    return [print("{}: {}".format(i, a_dictionary[k])) for i in
            sorted(a_dictionary)]
