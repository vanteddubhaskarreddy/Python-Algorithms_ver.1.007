class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = defaultdict(int)
        sm = 0
        for i in grid:
            s = ','.join(str(k) for k in i)
            d[s] +=1
        gridt = [[row[i] for row in grid] for i in range(len(grid))]
        for j in gridt:
            ts = ','.join(str(l) for l in j)
            if ts in d:
                sm+=d[ts]
        return sm