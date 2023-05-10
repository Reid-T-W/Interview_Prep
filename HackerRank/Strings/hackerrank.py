#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    # Write your code here
    hackerrank = 'hackerrank'
    hackerrank_iter = 0
    s_iter = 0
    string = []
    while s_iter < len(s) and hackerrank_iter < len(hackerrank):
        if s[s_iter] == hackerrank[hackerrank_iter]:
            string.append(s[s_iter])
            s_iter += 1
            hackerrank_iter += 1
        else:
            s_iter += 1
    if "".join(string) == hackerrank:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
