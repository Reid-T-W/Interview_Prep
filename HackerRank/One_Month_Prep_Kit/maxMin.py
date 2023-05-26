#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    # Sliding Window Approach (works but exceeds time limit)
    i = 0
    arr.sort()
    minimum = max(arr)
    while i + k <= len(arr):
        # slice_object = slice(i, i + k)
        # sliced = arr[slice_object]
        # diff = max(sliced) - min(sliced)
        diff = arr[i + k - 1] - arr[i]
        if diff < minimum:
            minimum = diff
        i += 1
    return minimum

    # Heap based approach
    # smallest = []
    # heapq.heapify(arr)
    # for _ in range(k):
    #     smallest.append(heapq.heappop(arr))
    # print(smallest)
    # print(max(smallest) - min(smallest))
    # return max(smallest) - min(smallest)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
