class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        d = defaultdict(int)
        l = r = c =0
        for r in range(len(s)):
            d[s[r]] += 1
            while d[s[r]] > 1:
                d[s[l]] -= 1
                l += 1
            c = max(c,r-l+1)
        return c







        
        
        # d = defaultdict(int)
        # i = 0
        # c = 0
        # j = 0
        # while j < len(s):
        #     # print(len(d), d, i, j)
        #     if d[s[j]] == 1:
        #         c = max(c, len(d))
        #         i = i+1
        #         j = i
        #         d = defaultdict(int)
        #         continue
        #     # else:
        #     d[s[j]] += 1
        #     j+=1
        # return max(c, len(d)) if len(s) > 1 else len(s)