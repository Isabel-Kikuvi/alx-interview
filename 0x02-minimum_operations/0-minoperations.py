#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculate the fewest no of ops needed to result in exactly n H characters.
    """
    if n < 2:
        return 0
    else:
        h_counter = 1
        opers = 1
        copy_size = 1

        while h_counter != n:
            if ((n % h_counter) == 0) and (h_counter != 1):
                copy_size = h_counter
                h_counter += copy_size
                opers += 2
            else:
                h_counter += copy_size
                opers += 1

    return opers
