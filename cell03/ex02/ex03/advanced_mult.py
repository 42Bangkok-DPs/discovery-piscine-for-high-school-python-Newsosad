#!/usr/bin/env python3
table = 0
while table <= 10:
    print(f"Table de {table}:", end=" ")
    multiplier = 0
    while multiplier <= 10:
        result = table * multiplier
        print(result, end=" ")
        multiplier += 1
    print()
    table += 1
