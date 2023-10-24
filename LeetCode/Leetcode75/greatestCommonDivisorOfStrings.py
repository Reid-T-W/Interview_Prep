class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
        (i.e., t is concatenated with itself one or more times). Given two strings 
        str1 and str2, return the largest string x such that x divides both str1 and str2.
        """
        def check(str_shortest, str_original_shortest, str_longest):
            if str_shortest == "":
                return ""
            if (len(str_longest) % len(str_shortest) != 0) or (len(str_original_shortest) % len(str_shortest) != 0):
                return check(str_shortest[0:-1], str_original_shortest, str_longest)
            multiplier_longest = int(len(str_longest) / len(str_shortest))
            multiplier_shortest = int(len(str_original_shortest) / len(str_shortest))
            if (str_shortest * multiplier_longest) == str_longest and (str_shortest * multiplier_shortest == str_original_shortest):
                return str_shortest
            else:
                return check(str_shortest[0:-1], str_original_shortest, str_longest)
            
        if len(str1) < len(str2):
            return check(str1, str1, str2)
        else:
            return check(str2, str2, str1)
            
sol = Solution()
print(sol.gcdOfStrings("ABAB", "ABABAB"))
print(sol.gcdOfStrings("ABC", "ABCABC"))
print(sol.gcdOfStrings("LEET", "CODE"))
# sol.gcdOfStrings("ABAB", "ABABAB")