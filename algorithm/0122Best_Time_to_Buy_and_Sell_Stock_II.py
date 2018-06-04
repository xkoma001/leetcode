class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        m_len = len(prices)
        buy, sell = [0] * m_len, [0] * m_len

        max_profit = 0
        buy[0] = -prices[0]
        for i in range(1, m_len):
            sell[i] = buy[i-1] + prices[i]
            max_profit = max(sell[i], max_profit)
            buy[i] = -prices[i]
            for j in range(1, i):
                buy[i] = max(sell[j]-prices[i], buy[i])
            buy[i] = max(buy[i-1], buy[i])
        return max_profit

    def maxProfit2(self, prices):
        if not prices:
            return 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i]-prices[i-1]
        return res
