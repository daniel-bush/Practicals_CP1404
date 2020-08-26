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
    quick_picks = int(input("How many quick picks? "))


def number_selection() -> list:
    line = []
    for i in NUMBERS_PER_LINE:
        number = randint(LOWEST_VALUE, HIGHEST_VALUE)
        line.append(number)
    return line



main()