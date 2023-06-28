#!/bin/python3
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        You are given an integer array coins representing coins
        of different denominations and an integer amount representing
        a total amount of money.Return the fewest number of coins 
        that you need to make up that amount. If that amount of money 
        cannot be made up by any combination of the coins, return -1.
        You may assume that you have an infinite number of each kind of coin.
        Time complexity (with memoization) = O(amount) - (needs checking)
        Time complexity (without memoization) = O(len(coins)^amount) - (needs checking)
        Space complexity = O(amount) - needs checking
        """
        memo = {}
        return self.findMinNumCoins(coins, amount, memo)
        
    def findMinNumCoins(self, coins, amount, memo):
        if amount in memo:
            return memo[amount]
        # base case
        if amount == 0:
            return 0 
        if amount < 0:
            return -1

        if amount in memo:
            return memo[amount]
        
        remaining = []
        for coin in coins:
            # Only append the postive values, since we do not want
            # -1 appended to the list
            value = self.findMinNumCoins(coins, amount - coin, memo)
            if value >= 0:
                remaining.append(value)
        # If remainig has values, the min value must be returned, since
        # we are looking for the fewest number of coins
        if remaining:
            return_val = min(remaining) + 1
            memo[amount] = return_val
            return (return_val)
        # If remaing is empty it means no possible solutions were found
        # hence we return -1
        value = -1
        memo[amount] = value
        return -1



sol = Solution()
print(sol.coinChange([1,2,5], 11))
print(sol.coinChange([2], 3))
print(sol.coinChange([1], 0))
print(sol.coinChange([1, 2, 5], 5))