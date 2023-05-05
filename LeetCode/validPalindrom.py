#!/usr/bin/env python3
import re
import math



def isPalindrom(self, s: str) -> bool:
    s = s.lower()
    final = "".join(re.findall(r'[a-zA-Z0-9*]', s))
    print(final)
    len_string = len(final)
    half_len = math.floor(len_string/2)
    print(len_string, half_len)
    palindrom = True
    for i in range(0, half_len):
        j = len - i
        if final[i] != final[j]:
            palindrom = False
            return palindrom
        return palindrom
s = "A man, a plan, a canal: Panama"
value = isPalindrom(s)