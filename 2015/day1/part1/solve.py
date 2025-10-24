#!/usr/bin/python3

"""

( -> go up one floor
) -> go down one floor

process one parantheses at a time

"""
floor = 0

with open("input.txt", "r") as input_file:
    for paren in input_file.read():
        if paren == "(":
            floor += 1
            print(f"Santa went up a floor, encountered {paren} -> {floor}")
        if paren == ")":
            floor -= 1
            print(f"Santa went down a floor, encountered {paren} -> {floor}")

