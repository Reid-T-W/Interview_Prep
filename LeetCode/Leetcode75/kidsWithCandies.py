from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find max
        return_list = []
        max_candies = max(candies)

        for candy in candies:
            if candy + extraCandies >= max_candies:
                return_list.append(True)
            else:
                return_list.append(False)
        return return_list
        
sol = Solution()
candies=[2,3,5,1,3]
extraCandies = 3
print(sol.kidsWithCandies(candies, extraCandies))