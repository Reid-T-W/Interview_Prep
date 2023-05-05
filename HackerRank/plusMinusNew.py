#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def format(num):
    return float("{:6f}".format(num))
def plusMinus(arr):
    # Write your code here
    zero = 0 
    postive = 0 
    negative = 0
    total = len(arr)
    for num in arr:
        if num == 0:
            zero += 1
        elif num > 0:
            postive += 1
        else:
            negative += 1
    return[format(postive/total), format(zero/total), format(negative/total)]

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(plusMinus(arr))
