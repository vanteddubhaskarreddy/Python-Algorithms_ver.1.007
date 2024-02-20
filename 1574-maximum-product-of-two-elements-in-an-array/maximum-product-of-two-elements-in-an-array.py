class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m=0
        n=0
        for i in nums:
            if i>n:
                if i>m:
                    n = m
                    m = i
                else:
                    n = i
        return (m-1)*(n-1)