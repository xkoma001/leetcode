class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = i
        for i in range(m+1):
            dp[0][i] = i

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[n][m]
