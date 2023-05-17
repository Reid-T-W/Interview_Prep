#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    """
    Given  and , find and print the minimum number
    of pages that must be turned in order to arrive at page .
    Args:
        n int: number of pages
        p int: desired page number
    Return:
        number of flips required to reach p: int
    """
    if p == 1:
        return 0
    if p % 2 != 0 and n - p == 1:
        return 1
    # Starting flipping from the Front
    no_front_flips = p // 2 if p % 2 == 0 else (p - 1) // 2 
    # Start flipping from the Back
    no_back_flips = (n - p) // 2
    return min(no_front_flips, no_back_flips)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
