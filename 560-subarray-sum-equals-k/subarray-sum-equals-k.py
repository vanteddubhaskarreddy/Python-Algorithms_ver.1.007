class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = defaultdict(int)
        ans[0] = 1
        s = c = 0
        for i in nums:
            s+=i
            c+=ans[s-k]
            ans[s]+=1
        return c