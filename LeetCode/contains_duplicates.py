#!/usr/bin/env python3
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))

# nums = [1,2,3,1]
nums = [1,2,3,4]
print(containsDuplicate(nums))