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

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    total = len(arr)
    for num in arr:
        if num == 0:
            zero += 1
        elif num < 0:
            neg += 1
        else:
            pos += 1
    print("{:.6f}".format(pos/total))
    print("{:.6f}".format(neg/total))
    print("{:.6f}".format(zero/total))  

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)