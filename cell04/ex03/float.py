#!/usr/bin/env python3
def isdecimal(numstr):
    try:
        float(numstr)
        return True
    except ValueError:
        return False
if __name__ == "__main__":
    numstr = input("Give me a number: ")
if isdecimal(numstr):
    print("This number is an decimal")
else:
    print("This number is a decimal")
