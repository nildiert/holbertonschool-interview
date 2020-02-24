#!/usr/bin/python3
""" Min value """


def factor(num):
    """ Return factors of number """
    prime_list = []
    value = num
    i = 1
    while value != 1:
        i += 1
        if value % i == 0:
            while (value % i == 0 and value != 1):
                value /= i
                prime_list.append(i)

    return prime_list


def minOperations(n):
    if n < 2 or type(n) is not int:
        return 0
    values = factor(n)
    return sum(values)
