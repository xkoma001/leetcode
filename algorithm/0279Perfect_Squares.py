class Solution:
    dp = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[1] = 1

        for i in range(1, n+1):
            if i*i <= n:
                dp[i*i] = 1
            if dp[i] == 1:
                continue
            dp[i] = dp[1]+dp[i-1]
            for j in range(2, (i//2)+1):
                dp[i] = min(dp[i], dp[j]+dp[i-j])
        return dp[n]

    def numSquares2(self, n):
        dp = [i for i in range(n+1)]
        for i in range(1, n+1):
            j = 1
            while i - j*j >= 0:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[n]

    def numSquares3(self, n):
        if n <= 0:
            return self.dp[0]
        while len(self.dp) <= n:
            m = len(self.dp)
            j = 1
            cur_min = m
            while j*j <= m:
                cur_min = min(cur_min, self.dp[m-j*j]+1)
                j += 1
            self.dp.append(cur_min)
        return self.dp[n]



