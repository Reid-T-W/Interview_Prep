#!/usr/bin/env python3
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = []
    anagrams = {}
    for str in strs:
        key = ''.join(sorted(str))
        if key not in anagrams.keys():
            anagrams[key] = [str]
        else:
            anagrams[key].append(str)
    
    result = [value for value in anagrams.values()]     
    return result


strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]
result = groupAnagrams(strs)
print(result)