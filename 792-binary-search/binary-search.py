class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums)-1
        while h>=l:
            
            mid = (l+h)//2
            print(nums)
            print(target)
            print(mid)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                h = mid - 1
            
            else:
                l = mid + 1
            
        return -1