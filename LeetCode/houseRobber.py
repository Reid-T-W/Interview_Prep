#!/bin/python3
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        first_lead_max = 0
        second_lead_max = 0
        for i, num in enumerate(nums):
            value = max(num + first_lead_max, second_lead_max)
            first_lead_max = second_lead_max
            second_lead_max = value
        return second_lead_max
    
sol = Solution()
# houses = [2,7,9,3,1]
houses = [1,2,3,1]
print(sol.rob(houses))