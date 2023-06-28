#!/bin/python3
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find the subarray
        with the largest sum, and return its sum.
        Time Complexity: O(n)
        """
        localMaxSum = nums[0]
        globalMaxSum = nums[0]
        # Iterate through every element in the array and find
        # the local max sum for every position, based on that find
        # the global max sum.
        for num in nums[1:]:
            if num > localMaxSum + num:
                localMaxSum = num
            else:
                localMaxSum += num
            if localMaxSum > globalMaxSum:
                globalMaxSum = localMaxSum
        return globalMaxSum

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))