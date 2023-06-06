#!/usr/bin/python3
for fst_digit in range(0, 10):
    for sec_digit in range(fst_digit + 1, 10):
        if fst_digit == 8 and sec_digit == 9:
            print("{}{}".format(fst_digit, sec_digit))
        else:
            print("{}{}".format(fst_digit, sec_digit), end=", ")
