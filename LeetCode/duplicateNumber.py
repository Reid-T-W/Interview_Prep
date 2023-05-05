#!/usr/bin/env python3
from typing import List

def findDuplicate(nums: List[int]) -> int:
    nums = sorted(nums)
    for ind in range(len(nums) - 1):
        if nums[ind] == nums[ind + 1]:
            return nums[ind]
        


nums = [1,3,4,2,2]
print(findDuplicate(nums))

nums = [3,1,3,4,2]
print(findDuplicate(nums))
