#!/usr/bin/python

def divisible_by_2(my_list=[]):
    """ Finds all multiples of 2 in a list """

    new_list = []

    for i in range(len(my_list)):
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_lst.append(False)
