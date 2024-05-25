class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxc = maxsofar = 0
        for i in range(1,len(prices)):
            # print(i)
            maxc = max(0, maxc+prices[i]-prices[i-1])
            maxsofar = max(maxc, maxsofar)
        return maxsofar