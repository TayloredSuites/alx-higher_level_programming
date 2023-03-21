#!/usr/bin/python3
if __name__ == "__main__":
    """Print infinite adtion of all args"""
    import sys

    addition = 0

    for i in range(1, len(sys.argv)):
        addition += int(sys.argv[i])
        print(addition)
