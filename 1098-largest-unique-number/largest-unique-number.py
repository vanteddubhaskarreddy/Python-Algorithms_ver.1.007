class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        max = float(-inf)
        for i in nums:
            if i>max and c[i] == 1:
                max = i
        return max if max > float(-inf) else -1