class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = {'a', 'e', 'i', 'o', 'u'}
        j = 0
        r = 0
        mr = 0
        for a in range(k):
            if s[a] in vow:
                r+=1
        mr = r
        for i in range(k, len(s)):
            print(i, j, s[i], s[j], r, mr)
            if s[i] in vow:
                r+=1
            if s[j] in vow:
                r-=1
            j+=1
            mr = max(mr,r)
        return mr