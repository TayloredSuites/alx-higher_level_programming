#!/usr/bin/python3

for i in range(1, 101, 1):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)
