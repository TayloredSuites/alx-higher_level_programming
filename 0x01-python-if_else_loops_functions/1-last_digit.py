#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
last_dgt = number % 10

if number < 0:
    last_dgt = (abs(number) % 10) * -1
    print("Last digit of {} is {} and is less than 6 and not 0".format(
        number, last_dgt))
if last_dgt > 5:
    print("Last digit of {} is {} and is greater than 5".format(
        number, last_dgt))
elif last_dgt == 0:
    print("Last digit of {} is {} and is 0".format(number, last_dgt)i)
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(
        number, last_dgt))
