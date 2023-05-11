#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    """
    Given a string s, determine if the string is
    "Funny" or "Not Funny"
    """
    # Write your code here
    # Reverse the strings
    s_reverse = ""
    s_asci = []
    s_rev_asci =[]
    for char in s[::-1]:
        s_reverse += char
    # s_reverse += s[0]
    # Get the ascii numbers
    for char in s:
        s_asci.append(ord(char))
    for rev_char in s_reverse:
        s_rev_asci.append(ord(rev_char))

    # Finding the absolute diff
    i = 0
    while i + 1 < len(s):
        s_diff = abs(s_asci[i] - s_asci[i + 1])
        s_rev_diff = abs(s_rev_asci[i] - s_rev_asci[i + 1])
        if s_diff != s_rev_diff:
            return "Not Funny"
        i += 1
    return "Funny"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
