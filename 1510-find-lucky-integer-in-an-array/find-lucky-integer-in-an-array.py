from collections import *
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = defaultdict(int)
        a=[]
        for i in arr:
            d[str(i)]+=1
        for i,j in d.items():
            if int(i) == int(j):
                 a.append(int(i))
        return max(a) if a else -1