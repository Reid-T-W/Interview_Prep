#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    """
    Given a list of queries, perform each query and
    poplute an answers array.
    Args:
        n int: array size
        queries array: list of all queries
    Returns:
        Answers array: array
    """
    # Write your code here
    lastAnswer = 0
    arr = [[] for _ in range(n)]
    answers = []
    for query in queries:
        x = query[1]
        y = query[2]
        idx = (( x ^ lastAnswer ) % n)
        if query[0] == 1:
            arr[idx].append(y)
        elif query[0] == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]            
            answers.append(lastAnswer)
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
