class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        minimum_buy = prices[0]

        for sell in prices:
            max_profit = max(max_profit, sell - minimum_buy)
            minimum_buy = min(minimum_buy, sell)

        return max_profit        