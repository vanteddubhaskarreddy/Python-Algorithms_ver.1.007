class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        elif t == '':
            return False
        d = {}
        for i in range(len(s)):
            d[i] = s[i]
        c = 0
        for i in range(len(t)):
            # print(t[i],d[c],c)
            if t[i] == d[c]:
                c+=1
                if c ==len(s):
                    # print(c)
                    break
        return True if c == len(s) else False