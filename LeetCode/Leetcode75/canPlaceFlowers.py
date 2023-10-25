from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        You have a long flowerbed in which some of the plots are planted,
        and some are not. However, flowers cannot be planted in adjacent plots.

        Given an integer array flowerbed containing 0's and 1's, where 0 means 
        empty and 1 means not empty, and an integer n, return true if n new flowers 
        can be planted in the flowerbed without violating the no-adjacent-flowers 
        rule and false otherwise.
        """
        count = 0
        # handling the edge case where n = 0
        if n == 0:
            return True
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # Handling edge cases
                # handling edge case where flowerbed has only one space
                if len(flowerbed) == 1:
                    return True
                if i == 0 and flowerbed[i+1] == 0:
                    count += 1
                    # update the flowerbed, so that it won't be a double entry
                    # on the next iteration
                    flowerbed[i] = 1

                elif i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                    count += 1
                    # update the flowerbed, so that it won't be a double entry
                    # on the next iteration
                    flowerbed[i] = 1

                # Handling middle cases
                else:
                    if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        count += 1
                        # update the flowerbed, so that it won't be a double entry
                        # on the next iteration
                        flowerbed[i] = 1
            if count >= n:
                return True
        return False
        
                


sol = Solution()
# flowerbed = [1,0,0,0,1]
# flowerbed = [1,0,0,1]
flowerbed = [0,0,1,0]
n = 2
print(sol.canPlaceFlowers(flowerbed, n))
