class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        dp = [0] * row

        for j in range(col):
            for i in range(row):
                if i == 0 and j == 0:
                    dp[i] = grid[i][j]
                elif i == 0:
                    dp[i] = dp[i] + grid[i][j]
                elif j == 0:
                    dp[i] = dp[i-1] + grid[i][j]
                else:
                    dp[i] = min(dp[i-1], dp[i]) + grid[i][j]
        return dp[row-1]
