#!/usr/bin/python3

for tens in range(10):
for units in range(tens + 1, 10):
print("{:d}{:d}".format(tens, units), end=", " if tens < 8 else "\n")
