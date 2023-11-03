from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Given an integer array nums, move all 0's to the end 
        of it while maintaining the relative order of the 
        non-zero elements.

        Do not return anything, modify nums in-place instead.
        """
        # Approach 1 (My Approach)
        first_index = 0
        second_index = 1

        while second_index  < len(nums) and first_index < len(nums):
            if nums[first_index] == 0 and nums[second_index] != 0:
                nums[first_index], nums[second_index] = nums[second_index], nums[first_index]
            else: 
                if nums[first_index] != 0:
                    first_index += 1
                if nums[second_index] == 0:
                    second_index += 1
                if first_index == second_index:
                    second_index += 1
        return nums
    
        # Approach 2 (From Solution in Leetcode)
        # slow = 0
        # for fast in range(len(nums)):
        #     if nums[fast] != 0 and nums[slow] == 0:
        #         nums[slow], nums[fast] = nums[fast], nums[slow]

        #     # wait while we find a non-zero element to
        #     # swap with you
        #     if nums[slow] != 0:
        #         slow += 1


sol = Solution()
nums = [0,1,0,3,12]
print(sol.moveZeroes(nums))
nums = [0]
print(sol.moveZeroes(nums))
nums = [1]
print(sol.moveZeroes(nums))
nums = [2, 1]
print(sol.moveZeroes(nums))
nums = [4,2,4,0,0,3,0,5,1,0]
print(sol.moveZeroes(nums))
