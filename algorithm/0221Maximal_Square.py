class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        row, col = len(matrix), len(matrix[0])
        max_len = 0

        def square_len(i, j):
            dis = 0
            while True:
                for k in range(dis):
                    if j+dis-1 >= col or i+dis-1 >=row or matrix[i+k][j+dis-1] != '1' or matrix[i+dis-1][j+k] != '1':
                        dis -= 1
                        return dis
                dis += 1
            return dis

        for i in range(row):
            for j in range(col):
                max_len = max(max_len, square_len(i, j))
        return max_len * max_len

    def maximalSquare2(self, matrix):
        if not matrix:
            return 0

        max_len = 0
        row, col = len(matrix), len(matrix[0])
        pre, cur = [0]*row, [0]*row
        for k in range(row):
            pre[k] = 0 if matrix[k][0] == '0' else 1
            max_len = max(pre[k], max_len)

        for j in range(1, col):
            cur[0] = 0 if matrix[0][j] == '0' else 1
            max_len = max(cur[0], max_len)
            for i in range(1, row):
                cur[i] = 0 if matrix[i][j] == '0' else min(pre[i], cur[i-1], pre[i-1])+1
                max_len = max(cur[i], max_len)
            for k in range(row):
                pre[k] = cur[k]
        return max_len * max_len
