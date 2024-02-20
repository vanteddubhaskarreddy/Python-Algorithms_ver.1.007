class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        s = 0
        n = 0
        for i in nums:
            s = s+i
            if s == 0:
                n+=1
        return n