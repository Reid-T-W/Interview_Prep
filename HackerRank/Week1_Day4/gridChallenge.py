#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    """
    Given a square grid of characters in the range 
    ascii[a-z], rearrange elements of each row 
    alphabetically, ascending. Determine if the 
    columns are also in ascending alphabetical order, 
    top to bottom.
    Args:
        grid: square grid
    Return:
        YES or NO
    """
    # Write your code here

    # sort the elements in every row of the
    # grid
    for i, row in enumerate(grid):
        row = list(row)
        row.sort()
        grid[i] = row


    for i in range(len(grid[0])):
        concat_str = ""
        for j in range(len(grid)):
            # Check if it respects the sorted order before
            # appending it to the string, if not return NO
            if concat_str and concat_str[-1] > grid[j][i]:
                return 'NO'
            concat_str += grid[j][i]
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
