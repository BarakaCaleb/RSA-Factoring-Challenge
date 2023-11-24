#!/usr/bin/python3
#Caleb Baraka <calebbaraka79@gmail.com>

"""Factorize given set of numbers in a file to form a product of two numbers"""
from sys import argv

def factorize(number):
    """Finds two small numbers that multiply to give the given number."""

    k = 2

    if number < 2:
        return

    while number % k:
        k += 1

    print("{:.0f}={:.of}*{:.0f}".format(number, number / k, k))


    if len(argv) != 2:
        exit()

    try:
        with open(argv[1]) as file:
            line = file.readline()

            while line != "":
                number = int(line.split('\n')[0])
                factorize(number)
                line = file.readline()
    except:
        pass
