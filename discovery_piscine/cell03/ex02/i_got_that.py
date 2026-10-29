#!/usr/bin/env python3

greet_ing = input("What you gotta say? : ")

while True:


    if greet_ing == "STOP":
    
        break

    elif greet_ing != "STOP":
       greet_ing = input("I got that! Anything else? : ")
       
       continue
