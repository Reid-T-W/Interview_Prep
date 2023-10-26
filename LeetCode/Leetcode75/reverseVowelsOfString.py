class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Given a string s, reverse only all the vowels
        in the string and return it. The vowels are 
        'a', 'e', 'i', 'o', and 'u', and they can appear
        in both lower and upper cases, more than once.
        """
        # Approach 1
        # # until a common point is reached, use two pointers
        # # to find and switch the vowels
        # vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        # reversed = [" "] * len(s)
        # start = 0
        # end = len(s) - 1

        # # Handling edge cases
        # if s == " ":
        #     return " "
        # if len(s) == 1:
        #     return s

        # while (start <= end):
        #     if s[start] not in vowels:
        #         reversed[start] = s[start]
        #         start += 1
        #     if s[end] not in vowels:
        #         reversed[end] = s[end]
        #         end -= 1
        #     if s[start] in vowels and s[end] in vowels:
        #         reversed[start] = s[end]
        #         reversed[end] = s[start]
        #         start += 1
        #         end -= 1        
        # return "".join(reversed)       

        # Approach 2
        # until a common point is reached, use two pointers
        # to find and switch the vowels
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        start = 0
        end = len(s) - 1

        # Handling edge cases
        if s == " ":
            return " "
        if len(s) == 1:
            return s
        
        s = list(s)

        while (start < end):
            if s[start] not in vowels:
                start += 1
            if s[end] not in vowels:
                end -= 1
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        
        return "".join(s)   

sol = Solution()
s = " "
print(sol.reverseVowels(s))

