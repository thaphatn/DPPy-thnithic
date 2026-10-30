#!/usr/bin/env python3

num_00 = [2, 8, 9, 48, 8, 22, -12, 2]
new_num = []

for num in num_00:
    if num > 5:
        new_num.append(num + 2)

new_num = set(new_num)

print(num_00)
print(new_num)