class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        cols, same_diag, same_diag1 = set(), set(), set()
        total = 0

        def total_queens(row):
            if row == n:
                nonlocal total
                total += 1
                return

            for col in range(n):
                if col not in cols and row-col not in same_diag and row+col not in same_diag1:
                    cols.add(col)
                    same_diag.add(row-col)
                    same_diag1.add(row+col)
                    total_queens(row+1)
                    cols.remove(col)
                    same_diag.remove(row-col)
                    same_diag1.remove(row+col)
            return

        total_queens(0)
        return total
