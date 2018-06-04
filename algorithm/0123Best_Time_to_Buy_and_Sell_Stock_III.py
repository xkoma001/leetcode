class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        k, m_len = 2, len(prices)

        dp = [[0 for _ in range(m_len)] for _ in range(k+1)]
        max_profit = 0

        for k in range(1, k+1):
            cur_max = -prices[0]
            for i in range(1, m_len):
                dp[k][i] = max(dp[k][i-1], cur_max+prices[i])
                cur_max = max(cur_max, dp[k-1][i]-prices[i])
                max_profit = max(max_profit, dp[k][i])

        return max_profit
