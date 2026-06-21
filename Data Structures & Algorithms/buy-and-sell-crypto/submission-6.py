class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxP = 0
        for p in prices:
            curr_profit = p - minBuy
            maxP = max(maxP, curr_profit)
            if p < minBuy:
                minBuy = p
        return maxP
