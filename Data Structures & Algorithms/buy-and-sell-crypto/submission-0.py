class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 1
        min_price = prices[0]
        profit = 0

        while r < len(prices):
            
            if prices[r] > min_price:
                profit = max(profit, prices[r]-min_price)
            
            else:
                min_price = prices[r]
            
            r += 1
        
        return profit

