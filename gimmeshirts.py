#!/usr/bin/env python3

def fizz_buzz(num):
    if num % 15 == 0:
        print("GimmeShirt")
    elif num % 5 == 0:
        print("Shirt")
    elif num % 3 == 0:
        print("Gimme")
    else:
        print(num)

for i in range(1, 101):
    fizz_buzz(i)
