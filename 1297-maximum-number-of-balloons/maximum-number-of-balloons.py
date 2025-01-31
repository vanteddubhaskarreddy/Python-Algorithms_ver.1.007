class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        l = ['b', 'a', 'l', 'l', 'o', 'o', 'n']
        c1 = Counter(l)
        c2 = Counter()
        for t in text:
            if t in c1:
                c2[t]+=1
        m=0
        while c2['l']>1:
            if c1 <= c2:
                c2-=c1
                m+=1
            else:
                break
        return m
        # return m if m<float(inf) else 0