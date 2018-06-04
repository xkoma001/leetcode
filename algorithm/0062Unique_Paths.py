class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0

        ans = [[0] * (n+1) for _ in range(m+1)]
        ans[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                ans[i][j] += ans[i-1][j] + ans[i][j-1]

        return ans[m][n]

    def uniquePaths2(self, m, n):
        if not m or not n:
            return 0

        ans = 1
        floor = 1
        for i in range(n-1):
            ans *= m+i
            floor *= i+1

        return ans//floor
