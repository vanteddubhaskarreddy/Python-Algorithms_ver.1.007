class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)-1
        # c = 0
        while s[l] == ' ':
            l-=1
        l1 = l
        try:
            while s[l] != ' ':
                l-=1
            return l1 - l
        except:
            return l1+1