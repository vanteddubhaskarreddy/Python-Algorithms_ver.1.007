class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        a = list(accumulate(nums)).count(0)
        return a