#!/usr/bin/python3

for first_digit in range(0, 10, 1):
    for second_digit in range(0, 10, 1):
        if first_digit < second_digit:
            print("{}{}".format(first_digit, second_digit), end=", ")
        else:
            print("", end="")
