class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max = 0
        while l < r:
            sum = min(height[l],height[r])*(r-l)
            if sum > max:
                max = sum
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        return max