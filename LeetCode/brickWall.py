#!/bin/python3
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        gaps = {}
        for row in wall:
            sum = 0
            for brick in row[0:-1]:
                sum += brick
                value = gaps.get(sum)
                if not value:
                    gaps[sum] = 1
                else:
                    gaps[sum] += 1
        if not gaps:
            return len(wall)
        
        # Sort the dict by values
        gaps_sorted = sorted(gaps.items(), key= lambda x:x[1], reverse=True)
        gaps_sorted = dict(gaps_sorted)
        key = list(gaps_sorted.keys())[0]

        # Get the minimum number of brick walls to break
        min_breaks = len(wall) - gaps_sorted[key]
        return min_breaks

# sol = Solution()
# sol.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]])

