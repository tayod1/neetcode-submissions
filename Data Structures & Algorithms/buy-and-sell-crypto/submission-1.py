class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        # initial min price
        minBuy = prices[0]

        # for each price
        for sell in prices:
            # update max profit = (curr_price - min_price)
            maxP = max(maxP, sell - minBuy)

            # update min price = min(min_price, curr_price)
            minBuy = min(minBuy, sell)
            
        return maxP
        





        