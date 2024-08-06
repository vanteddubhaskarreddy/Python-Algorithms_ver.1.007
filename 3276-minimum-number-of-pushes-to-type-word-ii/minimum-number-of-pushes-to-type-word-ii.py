class Solution:
    def minimumPushes(self, word: str) -> int:
        d = defaultdict(int)
        # l = ['']*7
        c = 0
        for x in word:
            d[x]+=1
        j = 1
        print(d)
        for i in range(len(d.keys())):
            maxk = max(zip(d.values(), d.keys()))[1]
            print(j, maxk, d[maxk])
            if j <= 8:
                c+=d[maxk]
            elif j <= 16:
                c+=2*d[maxk]
            elif j <= 24:
                c+=3*d[maxk]
            else:
                c+=4*d[maxk]
            print(c)
            j += 1
            del d[maxk]
        return c