class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left_pointer = 0
        right_pointer = 1

        max_profit = 0

        while right_pointer < len(prices):
            
            if prices[left_pointer] < prices[right_pointer]:
                profit = prices[right_pointer] - prices[left_pointer]
                
                if max_profit < profit:
                    max_profit = profit
            
            else:
                left_pointer = right_pointer

            right_pointer = right_pointer + 1

        return max_profit
            