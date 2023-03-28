#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """ Function that executes a function safely """

    try:
        result = fct(*args)
    except Exception as exp:
        print("Exception: {}".format(exp), file=sys.stderr)
        return None
    else:
        return result
