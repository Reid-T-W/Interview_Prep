#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    """
    Given an array of stones determine if a gem stone
    is present
    """
    # Write your code here
    arr_len = len(arr)
    mineral_dict = {}
    gemstone_count = 0
    for pos, stone in enumerate(arr):
        for min in stone:
            mineral_dict[min] = mineral_dict.get(min, [])+[pos]

    for key, value in mineral_dict.items():
        if len(set(value)) == arr_len:
            gemstone_count += 1
    return gemstone_count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
