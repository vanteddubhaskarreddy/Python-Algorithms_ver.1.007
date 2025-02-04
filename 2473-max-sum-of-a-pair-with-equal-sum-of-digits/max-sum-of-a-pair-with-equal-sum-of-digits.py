class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        maxs = float(-inf)
        for i in range(len(nums)):
            s = sum(list(int(i) for i in (''.join(str(nums[i])))))
            if s in d:
                maxs = max(maxs, nums[i]+d[s])
                d[s] = max(nums[i], d[s])
            else:
                d[s] = nums[i]
        return maxs if maxs != float(-inf) else -1