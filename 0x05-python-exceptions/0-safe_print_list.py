#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i])
    except IndexError as e:
        e.add_note("Index less than 1, out of bounds!")
        print(f'Caught {type(e)}: e')
