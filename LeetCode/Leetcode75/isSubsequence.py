class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if s is 
        a subsequence of t, or false otherwise.

        A subsequence of a string is a new string that 
        is formed from the original string by deleting 
        some (can be none) of the characters without 
        disturbing the relative positions of the remaining 
        characters. (i.e., "ace" is a subsequence of "abcde" 
        while "aec" is not).
        """
        s_pointer = 0
        t_pointer = 0
        count = 0
        if s == "":
            return True
        while (t_pointer < len(t) and s_pointer < len(s)):
            if s[s_pointer] == t[t_pointer]:
                count += 1
                s_pointer += 1
                t_pointer += 1
            else:
                t_pointer += 1
        return count == len(s)


sol = Solution()
s = "abc"
t = "ahbgdc"
print(sol.isSubsequence(s, t))

s = "axc"
t = "ahbgdc"
print(sol.isSubsequence(s, t))

s = ""
t = "ahbgdc"
print(sol.isSubsequence(s, t))

s = "b"
t = "abc"
print(sol.isSubsequence(s, t))