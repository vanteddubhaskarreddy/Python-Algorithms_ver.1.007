class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        pre = [0, nums[0]]
        for x in range(1,len(nums)):
            pre.append(pre[-1]+nums[x])
        
        res = [-1]*(len(nums))
        for i in range(k, len(nums)-k):
            res[i] = int((pre[i+k+1]-pre[i-k])//(k+k+1))
        return res