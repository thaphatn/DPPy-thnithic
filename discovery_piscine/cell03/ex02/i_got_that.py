#!/usr/bin/env python3


greet_ing = str(input("What you gotta say? : "))
while True:

    greet_ing = str(input("I got that! Anything else?  "))

    if greet_ing == "STOP":
    
        break

    elif greet_ing != "STOP":
       input("I got that! Anything else? : ")
