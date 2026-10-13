class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices)):
            j = i + 1
            while j < len(prices):
                curr_profit = prices[j] - prices[i]
                profit = max(curr_profit, profit)
                j += 1
        return profit
        





        