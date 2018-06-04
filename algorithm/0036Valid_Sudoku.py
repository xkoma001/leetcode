class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        if not board:
            return False
        line, col = 9, 9

        # horizontal
        lines, cols = set(), set()
        for i in range(line):
            lines.clear()
            cols.clear()
            for j in range(col):
                if board[i][j] != '.':
                    if board[i][j] not in lines:
                        lines.add(board[i][j])
                    else:
                        return False

                if board[j][i] != '.':
                    if board[j][i] not in cols:
                        cols.add(board[j][i])
                    else:
                        return False
        # square
        square = set()
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square.clear()
                for m in range(3):
                    for n in range(3):
                        if board[i+m][j+n] != '.':
                            if board[i+m][j+n] not in square:
                                square.add(board[i+m][j+n])
                            else:
                                return False

        return True

    def isValidSudoku2(self, board):
        if not board:
            return False

        m, n = len(board), len(board[0])
        row, col, cube = [[0] * m for _ in range(m)], [[0] * m for _ in range(m)], [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] != '.':
                    num, k = ord(board[i][j]) - ord('0')-1, i//3*3+j//3
                    if row[i][num] or col[j][num] or cube[k][num]:
                        return False
                    row[i][num] = col[j][num] = cube[k][num] = 1

        return True

if __name__ == '__main__':
    s = Solution()
    board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
    print(s.isValidSudoku2(board))
