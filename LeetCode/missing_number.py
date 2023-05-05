#!/usr/bin/env python3
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Approach 1
        sorted_nums = sorted(nums)
        # Checking if the first element is missing
        if sorted_nums[0] != 0:
            return 0
        for ind in range(len(sorted_nums)):
            # Checking if the last element is missing
            if ind == len(sorted_nums) - 1:
                return len(sorted_nums)
            # Checking if an element in between is missing
            diff = (sorted_nums[ind + 1]) - sorted_nums[ind]
            if ( diff != 1):
                return (sorted_nums[ind] + 1)
            
        # # Approach 2 (Formula approach)
        # le = len(nums)
        # su = (le * (le + 1)) // 2
        # li_sum = sum(nums)
        # return su - li_sum
    
        # # Approcah 3 (bit manimpulation)
        # miss_value = 0
        # miss_value_total = 0
        # for num in nums:
        #     miss_value ^= num
        # for nu in range(len(nums)+1):
        #     miss_value_total ^= nu
        # return miss_value ^ miss_value_total
            




sol = Solution()
# nums = [3,0,1]
# nums = [0,1]
# nums = [9,6,4,2,3,5,7,0,1]
nums = [[3,0,1], [0,1], [9,6,4,2,3,5,7,0,1]]
for num in nums:
# num = [0]
    print(sol.missingNumber(num))