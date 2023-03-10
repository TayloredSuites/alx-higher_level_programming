#!/usr/bin/python3

""" Function that checks for lower case character """
def islower(c):
    for c in range(65, 123, 1):
        if ord(c) < 97:
            print("False")
        else:
            print("True)
