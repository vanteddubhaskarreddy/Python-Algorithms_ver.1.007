class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = Counter()
        j = mc = 0
        for i in range(len(s)):
            while d[s[i]] > 0:
                d[s[j]] -= 1
                j+=1
            d[s[i]]=1
            mc = max(mc, i-j+1)
        return mc