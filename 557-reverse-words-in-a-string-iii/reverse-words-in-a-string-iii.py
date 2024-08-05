class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        for i in range(len(l)):
            l[i] = l[i][::-1]
        i = 1
        n = len(l)
        while i < 2*n-1:
            l.insert(i, ' ')
            i+=2
        return ''.join(l)