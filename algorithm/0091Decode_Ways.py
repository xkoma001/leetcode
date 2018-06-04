class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        l = len(s)
        dp = [0] * l
        dp[0] = 1

        for i in range(1, l):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if int(s[i-1:i+1]) <= 26 and s[i-1] != '0':
                if i < 2:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]
        return dp[l-1]
