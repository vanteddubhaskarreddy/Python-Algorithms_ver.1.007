class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in target:
            d1[i]+=1
        for j in arr:
            d2[j]+=1
        print(d1)
        print(d2)
        if d1 == d2:
            return True
        return False