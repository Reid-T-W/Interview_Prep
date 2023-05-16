#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    start = 0
    end = m
    no_of_ways_to_divide = 0
    for i in range(0, len(s)):
        seg_length = sum(s[start:end])
        if seg_length == d:
            no_of_ways_to_divide += 1
        start += 1
        end += 1
    return no_of_ways_to_divide


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
