class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        paths = [0] * m

        paths[0] = 1
        for col in range(n):
            for row in range(m):
                cur_val = 0
                if obstacleGrid[row][col] == 1:
                    paths[row] = 0
                    continue
                if row > 0 and obstacleGrid[row-1][col] != 1:
                    cur_val += paths[row-1]
                if col > 0 and obstacleGrid[row][col-1] != 1:
                    cur_val += paths[row]
                if col != 0 or row != 0:
                    paths[row] = cur_val

        return paths[m-1]

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0],[0]]))

