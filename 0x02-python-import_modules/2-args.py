#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    num_args = len(sys.argv)

    if num_args == 0:
        print("{} arguments".format(0))
    elif num_args == 1:
        print("{} argument:".format(1))
    elif num_args == 2:
        print("{} arguments:".format(2))
    else:
        print("{} arguments:".format(num_args - 1))
    for i in range(num_args - 1):
        print("{} : {}".format(1 + 1, sys.argv[i + 1]))
