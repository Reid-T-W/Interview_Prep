import itertools
from itertools import chain, zip_longest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        You are given two strings word1 and word2. Merge the 
        strings by adding letters in alternating order, starting 
        with word1. If a string is longer than the other, append
        the additional letters onto the end of the merged string.

        Return the merged string.
        """
        # Solution 1
        # merged = ""
        # for i in range(len(word1)):
        #     merged += word1[i]
        #     if i < len(word2):
        #         merged += word2[i]
        
        # # Check if word2 has remaining words
        # if len(word2) > len(word1) :
        #     merged += word2[i+1:]
        # return merged
    
        # Solution 2: Using zip
        merged = ""
        saved =  merged.join([x for x in itertools.chain.from_iterable(itertools.zip_longest(list(word1),list(word2))) if x])
        return saved
        

sol = Solution()
print(sol.mergeAlternately("abc", "pqrst"))
        
        