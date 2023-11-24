#!/usr/bin/python3

"""Factorize numbers in a file into a product of two prime numbers."""
import sys


def factorize():
    """Function to search fle and factorize the given set of numbers into two prime numbers (format n = p*q)"""
    try:
        file = sys.argv[1]
        with open(file) as f:
            for line_num in f:
                line_num = int(line_num)
                if line_num % 2 == 0:
                    print("{}={}*{}".format(line_num, line_num // 2, 2))
                    continue
                k = 3
                while k < line_num // 2:
                    if line_num % i == 0:
                        print("{}={}*{}".format(line_num, line_num // k, k))
                        break
                    k = k + 2
                if k == (line_num // 2) + 1:
                    print("{}={}*{}".format(line_num, line_num, 1))
    except (InderError):
        pass


    factorize()
