class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                profit = profit + 0
            else:
                profit = profit + prices[r] - prices[l]
            l = l + 1
            r = r + 1
        return profit
