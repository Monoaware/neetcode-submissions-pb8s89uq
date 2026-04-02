class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        
        for i in range(len(prices)):
            current_price = prices[i]
            
            for j in range(len(prices) - i):
                future_price = prices[j + i]
                current_profit = future_price - current_price

                if max_profit < current_profit:
                    max_profit = current_profit

        return max_profit
            
        