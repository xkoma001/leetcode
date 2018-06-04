class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        ans, direct = [], 0
        i, j = 0, -1
        op = [1, 1, -1, -1]

        m -= 1
        while True:
            dir = direct % 4
            if dir in {0, 2}:
                if n == 0:
                    break
                ans += [matrix[i][j+a*op[dir]] for a in range(1, n+1)]
                j += n*op[dir]
                n -= 1
            else:
                if m == 0:
                    break
                ans += [matrix[i+a*op[dir]][j] for a in range(1, m+1)]
                i += m*op[dir]
                m -= 1
            direct += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    a = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.spiralOrder(a))
