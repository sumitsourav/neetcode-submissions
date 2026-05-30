class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointer
        n = len(prices)
        l, r = 0 , 1
        res = 0
        while r < n:
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            r = r + 1
        return res
        
                