class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max=0
        smax=0
        for i in nums:
            if i>smax:
                if i>max:
                    smax = max
                    max = i
                else:
                    smax = i
        return (max-1)*(smax-1)