class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        m_len = len(prices)
        dp = [0] * m_len

        for i in range(1, m_len):
            dp[i] = dp[i-1]
            for j in range(0, i):
                if prices[i]-prices[j] > 0:
                    cur_max = prices[i]-prices[j]
                    if j >= 2:
                        cur_max += dp[j-2]
                    dp[i] = max(dp[i], cur_max)
        return dp[m_len-1]

    def maxProfit2(self, prices):
        if not prices:
            return 0
        m_len = len(prices)
        s, s1, s2 = 0, 0, 0
        b, b1 = -prices[0], -prices[0]

        for i in range(1, m_len):
            s = max(s1, b1+prices[i])
            b = max(b1, s2-prices[i])
            s2, s1 = s1, s
            b1 = b
        return s
