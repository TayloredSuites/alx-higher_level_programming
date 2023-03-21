#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """ Function that deletes a key in a dictionary
    Work on empty dict case """
    if key in a_dictionary:
        del a_dictionary[key]

        return (a_dictionary)
