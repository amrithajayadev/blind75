class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        profit = 0
        max_profit = 0
        max_price_after = [0]*len(prices)
        max_price_after[-1] = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            max_price_after[i] = max(prices[i], max_price_after[i+1])
        print(max_price_after)
        for i in range(0, len(prices)):
            max_profit = max(max_profit, max_price_after[i]-prices[i])

        return max_profit
