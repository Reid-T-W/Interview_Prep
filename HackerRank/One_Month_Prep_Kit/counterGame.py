#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Write your code here
    switch_turns = {'Louise': 'Richard', 'Richard': 'Louise'}
    player = 'Louise'
    # if n is 1 Richard wins since Louise cannot
    # make a move
    if n == 1:
        return 'Richard'
    
    log_n = math.log2(n)
    diff = log_n - int(log_n)

    # Iterate until you get a number that is 
    # a power of 2, while keeping track of the
    # players turn
    while diff != 0.0:
        n = n - pow(2, int(log_n))
        log_n = math.log2(n)
        player = switch_turns[player]
        diff = log_n - int(log_n)
    
    if log_n == 1:
        return player
    
    # log_n gives us the number of turns left
    # if number of turns is odd return the current
    # player
    if log_n % 2 != 0:
        return player

    player = switch_turns[player]
    return player

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
