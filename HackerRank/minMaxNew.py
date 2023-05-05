#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_sum = 0
    max_sum = 0
    # Sort the array
    sorted_array = sorted(arr)
    # To find the minimum sum the first 4 integers
    for i in range(4):
        min_sum += sorted_array[i]
    # To find the maximum sum the last 4 integers
    for j in range(4,0,-1):
        max_sum += sorted_array[j]
    print(f"{min_sum} {max_sum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
