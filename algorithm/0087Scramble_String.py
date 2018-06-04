class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m != n:
            return False
        dp = [[[False]*(m+1) for _ in range(n)] for _ in range(m)]

        # init
        for i in range(m):
            for j in range(n):
                dp[i][j][0] = True
                if s1[i] == s2[j]:
                    dp[i][j][1] = True

        for s in range(1, m+1):
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                        f = min(n-i, n-j, s)
                        for k in range(1, f):
                            dp[i][j][f] = (dp[i][j+f-k][k] and dp[i+k][j][f-k]) or (dp[i][j][k] and dp[i+k][j+k][f-k])
                            if dp[i][j][f]:
                                break
        return dp[0][0][m]

    def isScramble2(self, s1, s2):
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble2
        for i in range(1, n):
            if (f(s1[i:], s2[i:]) and f(s1[:i], s2[:i])) or (f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i])):
                return True
        return False
