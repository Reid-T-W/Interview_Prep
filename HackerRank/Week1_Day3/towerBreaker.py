#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    """
    Given n number of towers with m height each,
    two players are playing a game of towerbreakers.
    Determine which player wins
    Args:
        n int: number of towers
        m int: height of towers
    Returns:
        Winning player 1 or 2
    """
    # If number of towers is 0 or the height of a
    # of a tower equals 1, it means that player 1
    # can't make a move, hence player 2 automatically
    # wins
    if n == 0 or m == 1:
        return 2
    # If the number of towers is divisible by two
    # it is given that player 2 always wins, this holds
    # true whatever the height of the tower, since the
    # player is always making an optimal move (They always
    # reduce the height of the tower to one).
    if n % 2 == 0:
        return 2
    else:
        return 1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
