#!/usr/bin/python3
for first_digit in range(0, 9):
    for secound_digit in range(0, 10):
        if first_digit == 8 and secound_digit == 9:
            print(f"{first_digit}{secound_digit}")
        elif secound_digit > first_digit:
            print(f"{first_digit}{secound_digit}, ", end="")
