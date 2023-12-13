#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculate the fewest no of ops needed to result in exactly n H characters.
    """
    if n <= 1:
        return 0

    min_ops = [float('inf')] * (n + 1)
    min_ops[1] = 0

    for i in range(2, n + 1):
        for j in range(2, i + 1):
            if i % j == 0:
                min_ops[i] = min(min_ops[i], min_ops[j] + i // j)

    return min_ops[n]
