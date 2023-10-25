from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        There are n kids with candies. You are given an integer array candies, where
        each candies[i] represents the number of candies the ith kid has, and an 
        integer extraCandies, denoting the number of extra candies that you have.

        Return a boolean array result of length n, where result[i] is true if, after 
        giving the ith kid all the extraCandies, they will have the greatest number 
        of candies among all the kids, or false otherwise.
        
        Note that multiple kids can have the greatest number of candies.
        """
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