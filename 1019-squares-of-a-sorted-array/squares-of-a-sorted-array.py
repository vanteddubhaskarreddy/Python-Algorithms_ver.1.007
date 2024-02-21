class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # if len(nums) < 2:
        #     return [nums[0]*nums[0]]
        k = 0
        for k in range(len(nums)):
            if nums[k]>=0:
                break
        l = nums[k:]
        m = []
        if k > 0:
            m = [abs(a) for a in nums[k-1::-1] ]
        i = j = 0
        print(m)
        res = []
        while i<len(l) and j<len(m):
            if l[i] < m[j]:
                res.append(l[i]*l[i])
                i+=1
            else:
                res.append(m[j]*m[j])
                j+=1
        while i<len(l):
            res.append(l[i]*l[i])
            i+=1
        while j<len(m):
            res.append(m[j]*m[j])
            j+=1
        return res