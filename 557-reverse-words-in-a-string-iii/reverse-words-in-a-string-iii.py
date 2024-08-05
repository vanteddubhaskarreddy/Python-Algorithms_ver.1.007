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
        
        
        # l = r = 0
        # lis = s.split()
        # for i in range(len(lis)):
        #     lis[i] = list(lis[i])
        # for word in lis:
        #     l = 0
        #     r = len(word)-1
        #     print(word)

        #     for l in range(r):
        #         print(l, r)
        #         word[l],word[r] = word[r], word[l]
        #         r-=1
        # for i in range(len(lis)-1):
        #     lis.insert(i, ' ')
        # res = [j for sub in lis for j in sub]
        # return ''.join(res)