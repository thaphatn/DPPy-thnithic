#!/usr/bin/env python3

y = 0

while y <= 10:
    x = 0
    result = ""

    while x <= 10:
        result += str(y*x) + " "
        x += 1
    print(f"Table de {y}: {result}")
    y += 1