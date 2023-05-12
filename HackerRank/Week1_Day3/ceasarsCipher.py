#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    """
    Given a string s and a rotation factor k, convert the string
    into a ceasar cipher format, where every letter in s, is
    moved k times
    Args:
        s string to be encrypted
        k rotation factor
    Returns:
        encrypted string
    """
    # Write your code here
    cipher = ""
    for char in s:
            # Handling capital letters
            if re.match('[A-Za-z]', char):
                 asci_char = ord(char)
                 if (asci_char >= 65 and asci_char <= 90):
                      # Capital letter
                      initial_val = 65
                 elif (asci_char >= 97 and asci_char <= 122):
                      # Small letter
                      initial_val = 97                      
                 # Subtract initial_val from it in order to calculate the correct modules
                 asci_char -= initial_val
                 # Add the rotation value
                 adj_asci = asci_char + k
                 # Get the module (adj_asci % 26), since we have 26 letters
                 # and add initial_val to it in order to get which letter it maps to
                 # The modules is being done because we want to handle cases where k
                 # is very high, whatever the summed k we want it to map to the correc
                 # letter, so we work with the module instead
                 adj_asci = (adj_asci % 26) + initial_val
                 adj_char = chr(adj_asci)
                 cipher += adj_char
            else:
                 cipher += char
    return cipher
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
