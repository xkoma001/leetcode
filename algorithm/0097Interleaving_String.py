class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        m, n, q = len(s1), len(s2), len(s3)
        if m + n != q:
            return False

        dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(q+1)]

        # init
        for i in range(m+1):
            for j in range(n+1):
                dp[0][i][j] = 1

        for k in range(1, q+1):
            for i in range(0, k+1):
                j = k-i
                if i > m or j > n:
                    continue

                if j == 0:
                    if dp[k-1][i-1][j] == 1 and s1[i-1] == s3[k-1]:
                        dp[k][i][j] = 1
                elif i == 0:
                    if dp[k-1][i][j-1] == 1 and s2[j-1] == s3[k-1]:
                        dp[k][i][j] = 1
                else:
                    if dp[k-1][i-1][j] and s1[i-1] == s3[k-1]:
                        dp[k][i][j] = 1
                    elif dp[k-1][i][j-1] and s2[j-1] == s3[k-1]:
                        dp[k][i][j] = 1

        return True if dp[q][m][n] == 1 else False

    def isInterleave2(self, s1, s2, s3):
        m, n, q = len(s1), len(s2), len(s3)
        if m+n != q:
            return False
        dp = [[False] * (n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[m][n]


