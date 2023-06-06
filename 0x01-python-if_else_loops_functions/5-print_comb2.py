#!/usr/bin/python3
for counter in range(0, 100):
    if counter != 99:
        print("{:0>2.0f}".format(counter), end=", ")
    else:
        print("{}".format(counter))
