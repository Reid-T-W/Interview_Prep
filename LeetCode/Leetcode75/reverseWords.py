class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Given an input string s, reverse the order of the words.

        A word is defined as a sequence of non-space characters. 
        The words in s will be separated by at least one space.

        Return a string of the words in reverse order concatenated by a single space.
        """
        # Solution 1
        word = ""
        reversed = ""
        for letter in s:
            if letter == " ":
                if word != "":
                    reversed = self.appendToReversed(word, reversed)
                    word = ""
            else:
                word += letter
        if word != "":
            reversed = self.appendToReversed(word, reversed)
        return reversed
    
    def appendToReversed(self, word, reversed):
        if reversed != "":
            reversed = word + " " + reversed
        else:
            reversed = word + reversed
        return reversed

    
        # # Solution 2
        # s = s.split()
        # s = s[::-1]
        # s = " ".join(s)
        # return s
sol = Solution()
print(sol.reverseWords("a good   example"))
print(sol.reverseWords("  hello world  "))
print(sol.reverseWords("the sky is blue"))
print(sol.reverseWords("redi"))

