class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        n = len(prices)
        max_profit = 0
        pricess = (0,0)
        for i in range(n):
            for j in range(i+1,n):
                current_profit = prices[j] - prices[i]
                if current_profit > max_profit:
                    max_profit = current_profit
                    pricess = (i,j)
        print(pricess)
        return max_profit 
                