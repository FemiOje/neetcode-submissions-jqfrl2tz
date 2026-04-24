class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuyValue = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - minBuyValue
            maxProfit = max(maxProfit, profit)
            minBuyValue = min(prices[i], minBuyValue)

        return maxProfit
        
        