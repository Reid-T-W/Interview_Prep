#!/bin/python3

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add
        up to target.
        """

        # Create a dictionary that holds the index of
        # every element in the array
        indexs = {}
                
        # For every element in nums, check if the difference
        # with target is present in the dictionary
        # if not, store it and its index in the dictionary
        for i, num in enumerate(nums):  
            diff = target - num
            index = indexs.get(diff)
            if index is not None:
                return [i, index]
            indexs[num] = i

        
sol = Solution()

nums = [2, 7, 11, 15]
target = 9
print(sol.twoSum(nums, target))
