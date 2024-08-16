class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        c = Counter()
        for i in nums:
            c+=Counter(i)
        d = Counter((len(nums)-1)*list(c))
        c-=d
        return sorted([i for (i,j) in c.most_common()])