#!/bin/python3

import math
import os
import random
import re
import sys

def flippingMatrix(matrix):
    # Write your code here
    # Get the max elements to the first quadrant
    # Determine size of the quadrant
    size = len(matrix)/2
    sum=0
    # Get the max element from each col
    for i in (matrix):
        sum += max(i)
        # for j in range(len(i)):
    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()