class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic Programming
        n = len(prices)
        minBuy = prices[0]
        maxP = 0
        for i in range(n):
            profit = prices[i] - minBuy
            maxP = max(profit, maxP)
            if minBuy > prices[i]:
                minBuy = prices[i]
        return maxP
        
        
                