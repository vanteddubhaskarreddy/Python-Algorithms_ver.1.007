class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = ''
        if len(strs[0]) == 0:
            return a
        t = min(strs)
        for j in range(len(t)):
            for i in strs:
                if i[j] != t[j]:
                    return a
            a = a+t[j]
        return a