class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        slider = set()
        slider.add(nums[l])
        for r in range(1, len(nums)):
            
            while r - l > k:
                slider.remove(nums[l])
                l+=1
            if nums[r] in slider:
                return True
            slider.add(nums[r])
        return False            