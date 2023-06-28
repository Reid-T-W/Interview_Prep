#!/bin/python3
class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        """
        You are climbing a staircase. It takes n 
        steps to reach the top. Each time you can
        either climb 1 or 2 steps. In how many 
        distinct ways can you climb to the top?
        """
        # check if n is stored in memo
        if n in self.memo:
            return (self.memo[n])
        
        # base case
        # if n reaches 0 or 1 it means a solution has been
        # obtained (the starting point)
        if n == 0 or n == 1:
            return 1
        
        # call recursively
        # n can be reached from two positions, n - 1, n - 2
        # therefore we will recursively calculate the possibilities
        # for each.
        distinctPossibilities = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # Storing result in memo
        self.memo[n] = distinctPossibilities
        return distinctPossibilities
        
sol = Solution()
print(sol.climbStairs(5))