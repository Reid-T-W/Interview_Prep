#!/usr/bin/env python3
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # Fastest Approach
        # if not nums:
        #     return 0
        # length = 1
        # max_length = length
        # hash_set = set(nums)
        # for num in hash_set:
        #     if num - 1 in hash_set:
        #         continue
        #     while num + 1 in hash_set:
        #         length += 1
        #         num += 1
        #     if length > max_length:
        #         max_length = length
        #     length = 1
        # return max_length

        # Faster Approach
        # if not nums:
        #     return 0
        # length = 1
        # max_length = length
        # hash_set = set(nums)
        # for num in nums:
        #     if num - 1 in hash_set:
        #         continue
        #     while num + 1 in hash_set:
        #         length += 1
        #         num += 1
        #     if length > max_length:
        #         max_length = length
        #     length = 1
        # return max_length
        # Slow Approach

        # dict = {}
        # length = 1
        # max_length = 0
        # for n in nums:
        #     if dict.get(n-1) is None and dict.get(n+1) is None:
        #         dict[n] = 1
        #         length = 1
        #     else:
        #         dict[n] = 1
        #         # length = length + 1
        #         new_n = n - 1
        #         while(dict.get(new_n)):
        #             new_n = new_n - 1
        #         new_n = new_n + 1
        #         length = 0
        #         while(dict.get(new_n)):
        #             new_n = new_n + 1
        #             length = length + 1
        #     if length > max_length:
        #         max_length = length
        # return max_length

        # Ismaelis Solution
        max_length = 0
        start = 0
        end = start + 1
        hash_table = {num: False for num in arr}

        for num in arr:
            if not hash_table[num]:
                hash_table[num] = True
                lenght = 1

                if num - 1 in hash_table and hash_table[num  -1]:
                    lenght += 1
                    start = num -1

                if num + 1 in hash_table and hash_table[num + 1]:
                    lenght += 1
                    if start == 0:
                        start = num

                if lenght > max_length:
                    max_length = lenght
                    end = num

        return list(range(start, end + 1))


nums = []
# nums = [100,4,200,1,3,2]
# nums = [0,3,7,2,5,8,4,6,0,1]
# nums = [0, -1, -2, 4, -3]
# nums = [0, -1]
# nums = [1,3,5,2,4]
sol = Solution()
print(sol.longestConsecutive(nums))
