class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # nums.sort()
        res = nums.copy()
        pre = [0, nums[0]]
        for x in range(1,len(nums)):
            pre.append(pre[-1]+nums[x])
        for i in range(1, len(nums)):
            for j in range(i):
                res.append(pre[i+1] - pre[j])
        res.sort()
        return sum(res[left-1:right])%((10**9)+7)