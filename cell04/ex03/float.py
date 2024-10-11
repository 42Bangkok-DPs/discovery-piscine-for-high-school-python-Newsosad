#!/usr/bin/env python3
user_input = input("Give me a number: ")

try:
    number = float(user_input)
    message = f"this is an {'integer' if number.is_integer() else 'decimal'}."
    print(message)
except ValueError:
    print("That's not a valid number.")
