#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """ Finds all multiples of 2 in a list """

    new_list = []

    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
            """ print("{} is divisible by 2".format(i))
            truthful = [True for i in my_list if i % 2 == 0]
            print(truthful)
            even_numbers = list(filter(lambda x: x % 2 == 0, my_list)) """

        else:
            new_list.append(False)

            return new_list
