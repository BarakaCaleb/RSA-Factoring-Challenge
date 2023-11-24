#!/usr/bin
# caleb Baraka
# calebbaraka900@gmail.com

import sys

def factorize(number):
    """Generates two factors of a number given."""

    factor one = 2
    while (num % factor one):
        if (factor one <= number):
            factor one += 1

    factor two = number // factor one
    return (factor two, factor one)


if len(sys.argv) != 2:
    sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

    filename = sys.argv[1]

    file = open(filename, 'r')
    lines = file.readlines()

    for line in lines:
        number = int(line.rstrip())
        factor2, factor1 = factorize(number)
        print(f"{number} = {factor two} * {factor one}")
