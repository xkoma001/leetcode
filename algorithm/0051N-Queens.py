class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        board = ['.'*n for _ in range(n)]

        def queens(row, board, has_queen):
            if row == n:
                ans.append(board[:])
                return

            for col in range(n):
                meeting = False
                for (i, j) in has_queen:
                    if col == j or abs(col-j) == abs(row-i):
                        meeting = True
                        break
                if meeting:
                    continue

                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                has_queen.add((row, col))
                queens(row+1, board, has_queen)
                has_queen.remove((row, col))
                board[row] = '.'*n
            return

        queens(0, board, set())
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
