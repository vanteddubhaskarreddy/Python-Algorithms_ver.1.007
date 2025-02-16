class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = 0
        maxn = 0
        d = defaultdict(int)
        for j in range(len(nums)):
            d[nums[j]]+=1
            while d[nums[j]] > k:
                d[nums[i]]-=1
                i+=1
            maxn = max(maxn, 1+j-i)
        return maxn