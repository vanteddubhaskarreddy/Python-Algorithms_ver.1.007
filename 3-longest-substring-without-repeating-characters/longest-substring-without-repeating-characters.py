class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        i = 0
        c = 0
        j = 0
        while j < len(s):
            # print(len(d), d, i, j)
            if d[s[j]] == 1:
                c = max(c, len(d))
                i = i+1
                j = i
                d = defaultdict(int)
                continue
            # else:
            d[s[j]] += 1
            j+=1
        return max(c, len(d)) if len(s) > 1 else len(s)