#!/usr/bin/python3

def islower(c):
    for c in range(65, 123, 1):
        if ord(c) < 97:
            return False
        else:
            return True
