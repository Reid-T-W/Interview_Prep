#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigit(n, k):
    """
    Given a digit and the number of times to concatenate
    it, it returns its super digit.
    If n has only digit, then its super digit is n.
    Otherwise, the super digit of n is equal to the 
    super digit of the sum of the digits of n
    Args:
        n int: digit
        k int: number of times to concatenate
    Returns:
        The super digit
    """
    # Write your code here
    n_str = str(n)
    int_n = int(n_str)
    nums_list = [int(num) for num in str(int_n)] 
    int_n = sum(nums_list)
    total_sum = int_n * k 

    while total_sum >= 10:
        nums_list = [int(num) for num in str(total_sum)] 
        total_sum = sum(nums_list)
    return total_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
