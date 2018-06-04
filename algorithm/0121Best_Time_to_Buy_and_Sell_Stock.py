class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, prev_max = 0, 0
        day_len = len(prices)
        for i in range(1, day_len):
            prev_max = max(prev_max+prices[i]-prices[i-1], prices[i]-prices[i-1])
            max_profit = max(prev_max, max_profit)
        return max_profit

    def maxProfit2(self, prices):
        if not prices:
            return 0

        prev_min = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price > prev_min:
                max_profit = max(price-prev_min, max_profit)
            else:
                prev_min = price
        return max_profit
