#!/usr/bin/env python3

num_1 = int(input("Enter a number less than 25 \n"))

if num_1 > 25:
    print("Error")
else:
    while num_1 <= 25:
        print(f"Inside the loop, my variable is {num_1}")
        num_1 += 1