class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        val = nums[0]
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                val=nums[slow]
                slow += 1
        return slow