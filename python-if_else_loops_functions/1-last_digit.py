#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if abs(number) == number:
    sign = 1
    last_digit = sign * (number % 10)
elif number % 10 == 0:
    last_digit = number % 10
else:
    sign = -1
    last_digit = sign * (10 - (number % 10))

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif (last_digit < 6) & (last_digit != 0):
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
