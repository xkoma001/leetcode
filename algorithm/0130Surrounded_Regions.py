class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        di = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        path = set()

        def check_board(i, j):
            for (a, b) in di:
                if i+a < 0 or i+a >= m or j+b < 0 or j+b >= n:
                    return False
                if board[i+a][j+b] == 'X':
                    continue
                else:
                    if (i+a, j+b) not in path:
                        path.add((i+a, j+b))
                        if check_board(i+a, j+b):
                            return True
                        else:
                            return False
            return True

        for i in range(m):
            for j in range(n):
                if board[i][j] != 'X':
                    if check_board(i, j):
                        board[i][j] = 'X'
                    path.clear()
        return

    def solve2(self, board):
        if not board:
            return
        m, n = len(board), len(board[0])
        di = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        stack = []
        for i in range(m):
            if board[i][0] == 'O':
                stack.append((i, 0))
            if n > 1 and board[i][n-1] == 'O':
                stack.append((i, n-1))

        for j in range(1, n-1):
            if board[0][j] == 'O':
                stack.append((0, j))
            if m > 1 and board[m-1][j] == 'O':
                stack.append((m-1, j))

        while stack:
            i, j = stack.pop(0)
            if board[i][j] == 'O':
                board[i][j] = 'P'
                for (a, b) in di:
                    if 0 < i+a < m-1 and 0 < j+b < n-1:
                        stack.append((i+a, j+b))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'P':
                    board[i][j] = 'O'
        return

if __name__ == '__main__':
    s = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print(s.solve2(board))
