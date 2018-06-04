class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        totals = 0

        dis = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def helper(m, n):
            grid[m][n] = '0'
            for (x, y) in dis:
                if 0 <= m+x < row and 0 <= n+y < col and grid[m+x][n+y] == '1':
                    helper(m+x, n+y)
            return

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    totals += 1
                    helper(i, j)
        return totals
