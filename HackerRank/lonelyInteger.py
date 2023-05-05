#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def isEven(num):
    isEven = num%2 == 0
    # print(isEven)
    return (isEven)

def lonelyinteger(a):
    # Write your code here
    sorted_a = sorted(a)
    # print(sorted_a)
    for index in range(len(sorted_a)):
        # To avoid index out of bounds error
        if index == len(sorted_a) - 1:
            break
        # Ensure that the index is even and
        # Check if the value of the current index and next index are similar
        if isEven(index) and sorted_a[index] != sorted_a[index + 1]:
            return sorted_a[index]
    return sorted_a[index]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
