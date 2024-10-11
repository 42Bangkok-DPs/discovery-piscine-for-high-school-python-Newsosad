#!/usr/bin/env python3
called =  input("Enter a number less than 25: ")
called1 = int(called)

if called1 > 25: 
    print("Error")
else:
    while called1 <= 25:
        print(f"Inside the loop, my variable is {called1}")
        called1 +=1
