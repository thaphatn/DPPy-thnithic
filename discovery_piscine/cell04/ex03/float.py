#!/usr/bin/env python3

deci = float(input("Give me a number: "))

if deci.is_integer():
    print("This number is an integer")
else:
    print("This number is a decimal")