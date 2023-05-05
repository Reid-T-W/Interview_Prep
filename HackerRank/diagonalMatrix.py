#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diagonal1_sum = 0
    diagonal2_sum = 0
    # Sum the first diagonal
    for i in range(len(arr)):
        diagonal1_sum += arr[i][i]

    # Sum the second diagoal
    for j in range(len(arr) - 1,-1,-1):
        diagonal2_sum += arr[len(arr)-1-j][j]
    return abs(diagonal1_sum - diagonal2_sum)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
