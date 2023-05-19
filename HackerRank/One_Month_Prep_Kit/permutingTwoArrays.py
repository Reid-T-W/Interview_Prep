#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # Write your code here
    # Populate a diff_arr for A
    a_diff = []
    for num_a in A:
        if (k - num_a) >= 0:
            a_diff.append(k - num_a)
    
    a_diff.sort(reverse=True)
    B.sort()
    found = False

    # For each element in a_diff check if a corresponding 
    # element exists in B, the condition that must be satisfied
    # is element in B must be greater than or equal to the 
    # element in a_diff. This criteria should be satisfied for 
    # every element in a_diff, if not return 'NO'
    for num_a in a_diff:
        found = False
        if num_a <= 0:
            found = True
        for i in range(len(B)):
            # The first check is required because explored
            # elements in B will be marked as negative
            if B[i] >= 0 and B[i] >= num_a:
                B[i] = -B[i]
                found = True
                break
        if found == False:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
