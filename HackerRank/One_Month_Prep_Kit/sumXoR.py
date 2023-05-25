#!/bin/python3

import math
import os
import random
import re
import sys
# from itertools import combinations

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # Write your code here
    possible_answers = []
    binary_list = []
    binary_string = str(bin(n))
    binary_list = list(binary_string)[2:]
    # Get length of string so that it can be 
    # used to calculate the positions

    if n == 0:
        return 1
    
    length_binary_list = len(binary_list)
    current_power = length_binary_list - 1

    # Find the positions where the bit is 0, as these
    # are the possible places where xor and summation
    # can give the same value. And store their values in 
    # a list.
    for digit in binary_list:
        if digit == '0':
            possible_answers.append(pow(2, current_power))
        current_power -= 1

    # The list that was previously iterated represents, the
    # possible values that can be summed, but their combinations
    # can be summed to, hence the for loop below determines
    # all possible combinations we can sum
    total = 0
    n = len(possible_answers)
    n_factorial = math.factorial(len(possible_answers))
    for r in range(n):
        r = r + 1
        r_factorial = math.factorial(r)
        n_r_factorial = math.factorial(n - r)
        total += n_factorial / (r_factorial * (n_r_factorial))
   
    # Plus 1 is added to consider the case
    # when the value to be added is 0
    return int(total + 1)
                   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
