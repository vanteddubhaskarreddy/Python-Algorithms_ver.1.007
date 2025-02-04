class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sums = maxlen = 0
        seen = {0:-1}
        for i in range(len(nums)):
            sums = sums+1 if nums[i] == 1 else sums-1
            if sums in seen:
                maxlen = max(maxlen, i - seen[sums])
            else:
                seen[sums] = i
        return maxlen