#!/usr/bin/python3

def print_last_digit(number):
    digit = number % 10
    answer = print("{:02}".format(digit))
    return answer
