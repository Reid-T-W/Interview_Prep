#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    """
    Given a string s determine if the SOS message
    is corrupted
    """
    # Write your code here
    count = 0
    for index, char in enumerate(s):
        if index % 3 == 0 and char != 'S':
            count += 1
        elif index % 3 == 1 and char != 'O':
            count += 1
        elif index % 3 == 2 and char != 'S':
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
