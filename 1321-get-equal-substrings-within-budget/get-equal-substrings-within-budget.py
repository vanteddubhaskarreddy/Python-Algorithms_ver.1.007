class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        c = j = mc = 0
        def dif(i):
            return abs(ord(t[i]) - ord(s[i]))
        for i in range(len(s)):
            c += dif(i)
            while c > maxCost:
                c -= dif(j)
                j+=1
            mc = max(mc, i-j+1)
        return mc
            








        # while i < len(s):
        #     print(c, i, abs(ord(t[i]) - ord(s[i])))
        #     if c+abs(ord(t[i]) - ord(s[i])) > maxCost:
        #         break
        #     c += abs(ord(t[i]) - ord(s[i]))
        #     print(c, i, abs(ord(t[i]) - ord(s[i])))
        #     i+=1
        # return i