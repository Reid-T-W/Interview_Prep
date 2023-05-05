#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    # Check if its PM or AM
    is_pm = True if s[-2:]=="PM" else False
    hour = s[0:2]

    # if PM
    if is_pm:
        # Equal to 12
        if hour == '12':
            # Do Nothing
            conv_hour = hour
        # And not equal to 12
        else:
            # Add 12
            conv_hour = int(hour) + 12
    # If AM
    else:
        # Equal to 12
        if hour == '12':
            # Subtract 12
            conv_hour = str(0) + str(int(hour) - 12)
        # Not equal to 12
        else:
            conv_hour = hour
    return str(conv_hour)+s[2:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
