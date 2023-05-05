#!/bin/python3


import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    total_sum = sum(arr)

    # To find min sum, the highest element will be removed
    max_num = max(arr)
    min_sum = total_sum - max_num
    # To find max sum, the lowest element will be removed
    min_num = min(arr)
    max_sum = total_sum - min_num

    print(min_sum, max_sum)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


# Combinators Approach
from itertools import combinations


def miniMaxSum(arr):
    # print(combinations(arr, 4))
    combo_add = [print(sum(x)) for x in combinations(arr, 4)]

    # print(min(combo_add), max(combo_add), sep=" ")


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)