"""
121. Best Time to Buy and Sell Stock

Pattern: one pass, track the lowest price so far.
Approach: for each price, update the lowest price seen so far, then check the
profit if I had bought at that lowest price and sold today. Keep the biggest
profit. Return 0 if no profit is possible.

Time: O(n), one pass.
Space: O(1), a few variables.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        low = prices[0]
        best_profit = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            if prices[i] - low > best_profit:
                best_profit = prices[i] - low

        return best_profit
