class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = defaultdict(int)
        lis = []
        for i in range(len(arr)):
            d[arr[i]] += 1
        for i, j in d.items():
            if j == 1:
                lis.append(i)
        return lis[k-1] if k <= len(lis) else ''