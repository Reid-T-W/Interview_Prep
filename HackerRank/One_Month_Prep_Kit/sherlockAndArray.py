#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    left_sum = 0 * len(arr)
    right_sum = 0 * len(arr)

    last = len(arr) - 1

    for i in range(len(arr)):
        if i + 1 < len(arr):
            left_sum[i + 1] = left_sum[i] + arr[i]

            right_sum[last - (i + 1)] = right_sum[last - i] + arr[last - i]

    for j in range(len(left_sum)):
        if left_sum[j] == right_sum[j]:
            return 'YES'
    return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
