class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxs = collections.deque()
        res = []
        for i in range(len(nums)):
            while maxs and nums[i] > nums[maxs[-1]]:
                maxs.pop()
            maxs.append(i)
            if i > k-2:
                if maxs[0]+k-1 < i:
                    maxs.popleft()
                res.append(maxs[0])
        return [nums[j] for j in res]