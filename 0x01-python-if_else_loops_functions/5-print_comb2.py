#!/usr/bin/python3
for counter in range(0, 100):
    if counter < 10:
        print("0{}".format(counter), end="")
    else:
        print("{}".format(counter), end="")
    if counter != 99:
        print(", ", end="")
