class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        plw = Counter()
        pll = Counter()
        for i,j in matches:
            plw[i]+=1
            pll[j]+=1
        a = []
        a.append([])
        a.append([])
        pla = list(set(plw+pll))
        pl = Counter(pla)

        for k,l in (pll + pl).items():
            if l == 1:
                a[0].append(k)
            elif l == 2:
                a[1].append(k)
        a[0].sort()
        a[1].sort()
        return a