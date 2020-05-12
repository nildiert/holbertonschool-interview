#!/usr/bin/python3
""" Min value """


# def factor(num):
#     """ Return factors of number """
#     prime_list = []
#     value = num
#     i = 1
#     while value != 1:
#         i += 1
#         if value % i == 0:
#             while (value % i == 0 and value != 1):
#                 value /= i
#                 prime_list.append(i)

#     return prime_list

import math


def factors(n):

    factors = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n))+1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            factors.append(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        factors.append(n)
    return factors


def minOperations(n):
    if n < 2 or type(n) is not int:
        return 0
    values = factors(n)
    return int(sum(values))
