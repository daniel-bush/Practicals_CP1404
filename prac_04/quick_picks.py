"""
Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that
many lines of output. Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS.

Each line (quick pick) should not contain any repeated number.

Each line of numbers should be displayed in sorted (ascending) order.
"""
from random import randint

NUMBERS_PER_LINE = 6
LOWEST_VALUE = 1
HIGHEST_VALUE = 45


def main():
    no_of_lines = int(input("How many quick picks? "))
    line_values = []
    for i in range(no_of_lines):
        line = number_selection()
        line_values.append(line)
    print(line_values)


def number_selection() -> list:
    """Generates list of unique random integers within a specified range. Returns list."""
    line = []
    for i in range(NUMBERS_PER_LINE):
        not_unique = True
        while not_unique:
            number = randint(LOWEST_VALUE, HIGHEST_VALUE)
            if number not in line:
                line.append(number)
                not_unique = False
    line.sort()
    return line



main()