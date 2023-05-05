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
    # Identify if its PM or AM
    # Handling AM conversion
    if s[-2:] == 'AM':
        if s[0:2] == "12":
            return ("00" + s[2:8])
        else:
            return (s[0:8])

    # Handling PM conversion
    else:
        if s[0:2] == "12":
            return (s[0:8])
        else:
            converted = int(s[0:2]) + 12
            return (str(converted) + s[2:8])
    # Handling PM conversion

    # 12:00:00AM 00:00:00

    # 01:00:00AM 01:00:00
    # 11:00:00AM 11:00:00

    # 12:00:00PM 12:00:00

    # 01:00:00PM 13:00:00
    # 02:00:00PM 14:00:00
    # 11:00:00PM 23:00:00

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
