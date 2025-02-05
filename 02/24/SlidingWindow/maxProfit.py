from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Iterate through prices
        # keep track of historic profits using a maxprofit
        # keep track of min and max.
        # min -- max
        # if curr < min, set as new min
        # if curr > min AND index > minIndex, set as max, update max profit

        maxProfit = 0
        minIndex = 0
        maxIndex = 0
        for index, price in enumerate(prices):
            if price < prices[minIndex]:
                minIndex = index
            elif price > prices[minIndex] and index > minIndex:
                maxIndex = index
                maxProfit = max(maxProfit, prices[maxIndex] - prices[minIndex])

        return maxProfit
