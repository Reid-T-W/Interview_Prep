#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    # Convert arr to a set while maintaining order
    # arr_dict = dict(Counter(arr))
    # Populating the dict
    # Format {cash: [count, [index, index]]}
    arr_dict = {}
    for i, cash in enumerate(arr):
        if cash in arr_dict:
            arr_dict[cash][0] += 1
            arr_dict[cash][1].append(i)
        else: 
            arr_dict[cash] = [1, [i]]


    # Tracking the index
    index = 0
    for cash in arr:

        req = m - cash
        if req > 0:
            # Edge case: m = cash + req
            if req == cash and arr_dict.get(req)[0] > 1:
                one_index_first = arr_dict.get(req)[1][0] + 1
                one_index_second = arr_dict.get(req)[1][1] + 1
                return [one_index_first,  one_index_second]
            elif req != cash and arr_dict.get(req) != None:
                one_index_first = arr_dict[cash][1][0] + 1
                one_index_second = arr_dict[req][1][0] + 1
                return [one_index_first,  one_index_second]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # Reading from file
    rptr = open('input.txt', 'r')
    t =  int(rptr.readline())
    # Reading from command line
    # t = int(input().strip())

    for t_itr in range(t):

        # Reading from command line
        # m = int(input().strip())
        # n = int(input().strip())
        # arr = list(map(int, input().rstrip().split()))

        # Reading from file
        m =  int(rptr.readline())
        n =  int(rptr.readline())
        arr = list(map(int, rptr.readline().split()))

        result = icecreamParlor(m, arr)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
