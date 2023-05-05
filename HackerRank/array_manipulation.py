#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    
    # # First attempt (works but high time complexity)

    # indexs_dict = {}
    # if not queries:
    #     return 0
    # for item in queries:
    #     for index in range(item[0], (item[1] + 1)):
    #         if index in indexs_dict:
    #             indexs_dict[index] += item[2]
    #         else:
    #             indexs_dict[index] = item[2]
    # return max(indexs_dict.values())


    # Second attempt (Hackerrank approach passes all checks)

    indexs_dict = {}
    max = None
    sum = 0
    for item in queries:
        indexs_dict[item[0]] = indexs_dict.get(item[0], 0) + item[2]
        indexs_dict[item[1] + 1] = indexs_dict.get(item[1] + 1, 0) - item[2]
    indexes = sorted(indexs_dict.keys())
    for i in indexes:
        val = indexs_dict[i]
        sum += val
        if max is None or max < sum:
            max = sum
    return max

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fo = open('array_mani_tria_file.txt')
    first_line = fo.readline()
    first_multiple_input = first_line.rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, fo.readline().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
