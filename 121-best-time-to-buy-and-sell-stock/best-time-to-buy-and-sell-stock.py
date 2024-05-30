class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxc = maxsofar = 0
        # for i in range(1,len(prices)):
        #     # print(i)
        #     maxc = max(0, maxc+prices[i]-prices[i-1])
        #     maxsofar = max(maxc, maxsofar)
        # return maxsofar
        l = 0
        maxx = 0
        for r in range(1,len(prices)):
            profit = prices[r] - prices[l]
            if profit >= 0:
                maxx = max(maxx, profit)
            else:
                l = r
        return maxx
            