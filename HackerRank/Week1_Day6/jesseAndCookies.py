#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    heapq.heapify(A)
    operations = 0
    least_sweet_cookie = heapq.heappop(A)

    while least_sweet_cookie < k:
        if A:
            second_least_sweet_cookie = heapq.heappop(A)
            sweetness = (1 * least_sweet_cookie) + (2 * second_least_sweet_cookie)
            operations += 1
            heapq.heappush(A, sweetness)
            least_sweet_cookie = heapq.heappop(A)
        else:
            return -1

    return operations



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
