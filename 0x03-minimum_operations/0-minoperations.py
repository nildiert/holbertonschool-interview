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
    """calculates the factors of n number"""
    mylist = []
    while n % 2 == 0:
        mylist.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            mylist.append(i)
            n = n / i
    if n > 2:
        mylist.append(n)
    return mylist



def minOperations(n):
    if type(n) != int or n < 2:
        return 0
    numOperations = sum(factors(n))
    return int(numOperations)
