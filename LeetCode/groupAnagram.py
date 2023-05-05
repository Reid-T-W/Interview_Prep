#!/usr/bin/env python3
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = []
    anagrams = {}
    for index, str in enumerate(strs):
        key = ''.join(sorted(str))
        if key not in anagrams.keys():
            anagrams[key] = [index]
        else:
            anagrams[key].append(index)
    
    for value in anagrams.values():
        temp = []
        for ori_index in value:      
            temp.append(strs[ori_index])
        result.append(temp)
    return result


strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]
result = groupAnagrams(strs)
print(result)