class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        res = ''
        m = word2
        n = word1
        c = 0
        if len(word1) > len(word2):
            m = word1
            n = word2
            c = 1
        if c == 1:
            while j < len(n):
                res = res+m[i]+n[j]
                i,j = i+1,j+1
        else:
            while j < len(n):
                res = res+n[j]+m[i]
                i,j = i+1,j+1
        
        res = res + m[j:]
        return res