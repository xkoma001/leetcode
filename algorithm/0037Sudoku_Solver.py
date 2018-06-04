class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row, col = len(board), len(board[0])
        row_set = [set() for _ in range(row)]
        col_set = [set() for _ in range(col)]
        square_set = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(row):
            for j in range(col):
                if board[i][j] != '.':
                    cur_num = int(board[i][j])
                    row_set[i].add(cur_num)
                    col_set[j].add(cur_num)
                    square_set[i // 3][j // 3].add(cur_num)

        def helper(board, i, j):
            if i == row:
                return True
            if board[i][j] == '.':
                for k in range(1, 10):
                    if k not in row_set[i] and k not in col_set[j] and k not in square_set[i//3][j//3]:
                        board[i][j] = str(k)
                        row_set[i].add(k)
                        col_set[j].add(k)
                        square_set[i//3][j//3].add(k)
                        rel = False
                        if j == col-1:
                            rel = helper(board, i+1, 0)
                        else:
                            rel = helper(board, i, j+1)
                        if rel:
                            return True
                        board[i][j] = '.'
                        row_set[i].remove(k)
                        col_set[j].remove(k)
                        square_set[i//3][j//3].remove(k)
            else:
                rel = False
                if j == col - 1:
                    rel = helper(board, i + 1, 0)
                else:
                    rel = helper(board, i, j + 1)
                return rel
            return False
        helper(board, 0, 0)
        return

if __name__ == '__main__':
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(s.solveSudoku(board))
