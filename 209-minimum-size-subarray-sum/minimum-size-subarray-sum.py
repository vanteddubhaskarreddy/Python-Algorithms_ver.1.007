class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = s = 0
        res = len(nums)+1
        for i in range(len(nums)):
            s += nums[i]
            while s>=target:
                res = min(res, i-j+1)
                s -= nums[j]
                j+=1
        return res if res < len(nums)+1 else 0