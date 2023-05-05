#!/usr/bin/env python3
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        app = [[] for _ in range(len(nums) + 1)]
        result = []
        for item in nums:
            if item not in freq:
                freq[item] =  1
            else:
                freq[item] = freq[item] + 1
        for key, value in freq.items():
            app[value].append(key)
        index = len(nums)
        counter = 0
        while counter != k:
            if len(app[index]) != 0:
                # k += 1
                for item in app[index]:
                    result.append(item)
                    counter += 1
                if index == 0:
                    break
                index -= 1
            else:
                if index == 0:
                    break
                index -= 1
        return result
# array = [7, 1, 1, 1, 2, 2, 3, 7, 4, 4, 4]
# array = [4,1,-1,2,-1,2,3]
# array = [1]
array = [1,1,1,2,2,3]
k = 2
inst = Solution()
print(inst.topKFrequent(array, 2))