#!/usr/bin/env python3
import math

def round_up():
    userinput = input("Give me a number: ")

    try:
        num = float(userinput)
        roundednum = math.ceil(num)
        print(roundednum)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    round_up()
