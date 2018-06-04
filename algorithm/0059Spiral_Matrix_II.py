class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        if not n:
            return []

        matrix = [[0] * n for _ in range(n)]

        dix, diy = [0, 1, 0, -1], [1, 0, -1, 0]
        di, x, y = 0, 0, 0

        for i in range(1, n*n+1):
            matrix[x][y] = i
            if not (0 <= x+dix[di] <= n-1) or not (0 <= y+diy[di] <= n-1) or matrix[x+dix[di]][y+diy[di]] != 0:
                di += 1

            di = di % 4
            x += dix[di]
            y += diy[di]

        return matrix
