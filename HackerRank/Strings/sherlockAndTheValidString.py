#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    """
    Sherlock considers a string to be valid if all
    characters of the string appear the same number
    of times. It is also valid if he can remove just
    character at  index in the string, and the
    remaining characters will occur the same number 
    of times. Given a string , determine if it is valid.
    If so, return YES, otherwise return NO.
    Args:
        s string - string to be checked
    Return:
        YES string - if valid
        NO string - if not valid
    """
    # Write your code here
    # Populate the dictionary with the characters count
    from collections import Counter
    values_set = set()
    counted_dict = Counter(s)

    for digit in counted_dict.values():
        values_set.add(digit)
        # handle the case where there might be multiple
        # values of count, the maximum allowed values of 
        # count is 1
        # Ex: aabbbcccc
        if len(values_set) > 2:
            return 'NO'
        
    # Handling the case where all elements have the same
    # count
    if len(values_set) == 1:
        return "YES"
    
    # handle the case were items of the same count appear
    # multiple times
    # Ex: aabbbb aaaaab aabbccccccc
    max_value = max(values_set)
    min_value = min(values_set)
    diff = abs(max_value - min_value)
    # The first condition is added so that cases such as
    # aaaaab do not fail
    if  min_value != 1 and diff > 1:
        return ('NO')

    # Handling the case were the count difference is less
    # than one but different characters have the
    # same count, handles cases such as 'aabbcd', 'aabbcccddd', 'aaaaaccccdddd'
    # and 'aaaaabc'
    freq_count = Counter(counted_dict.values())

    # The first condition is added because we need to handle cases
    # with key one separtely, as we let them pass in a previous condition
    if freq_count.get(1, 0) > 1 or 1 not in freq_count.values():
        return 'NO'
    return ('YES')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # rdtr = open('./input.txt')
    # s = rdtr.read()
    # result = isValid(s)

    # fptr.write(result + '\n')

    # fptr.close()
