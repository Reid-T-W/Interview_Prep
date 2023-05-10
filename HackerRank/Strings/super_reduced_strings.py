#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    """
    Given a string s, it reduces it to a form where, there
    are no adjcent duplicate characters
    """
    # Write your code here
    pointer = 0
    chars = []
    # Loop through the string and append
    # each character to the stack. Check if
    # the character is similar to the top most
    # item in the stack.
    # If similar pop that item and do not append
    while pointer < len(s):
        if not chars:
            chars.append(s[pointer])
        else:
            if chars[-1] == s[pointer]:
                chars.pop()
            else:
                chars.append(s[pointer])
        pointer += 1
    if not chars:
        return 'Empty String'
    return ''.join(chars)
            
            


    # first = 0
    # second = 1
    # list = []
    # while second < len(s):
    #     if s[first] == s[second]:
    #         first += 2
    #         second += 2
    #     else:
    #         list.append(s[first])
    #         first += 1
    #         second += 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
