class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        if k == 1:
            return 0
        else:
            d = float(inf)
            i = 0
            j = k-1
            while j < len(nums):
                if nums[j]-nums[i] < d:
                    d = nums[j]-nums[i]
                    print(j)
                    print(nums[j],nums[i])
                    print(d)
                i,j = i+1,j+1
        return d