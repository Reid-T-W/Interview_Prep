#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    """
    There is a large pile of socks that must be 
    paired by color. Given an array of integers 
    representing the color of each sock, determine 
    how many pairs of socks with matching colors 
    there are.
    Args:
        n int: number of socks
        ar array: array of socks colors
    """
    pairs = 0
    i = 0
    ar.sort()
    if n == 0 or n == 1:
        return 0
    while i + 1 < n:
        if ar[i] == ar[i + 1]:
            pairs += 1
            i += 2
        else:
            i += 1
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
