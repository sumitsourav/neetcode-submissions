class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        n = len(prices)
        maxP = 0
        while r < n:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
            if prices[l] > prices[r]:
                l = r
                r = l + 1
            else:
                r= r + 1
        return maxP