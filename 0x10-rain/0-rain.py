#!/usr/bin/env python3
"""
Given a list of non-negative integers representing walls
of width 1, calculate how much water will be retained
after it rains.
"""


def rain(walls):
    """
    Args:
        walls - is a list of non-negative integers.
    Returns:
        If the list is empty return 0.
    """
    if type(walls) is not list:
        return 0
    if len(walls) is 0:
        return 0
    n = len(walls) - 1
    total_water = 0

    for i in range(1, n - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[j]

        for j in range(i + 1, n):
            right = max(right, walls[j])

        total_water += total_water + (min(left, right) - walls[j])
    return total_water
