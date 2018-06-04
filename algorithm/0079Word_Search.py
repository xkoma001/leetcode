class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        row, col = len(board), len(board[0])
        board_used = [[0] * col for _ in range(row)]

        def search_path(x, y, wd):
            if not wd:
                return True

            if 0 <= x < row and 0 <= y < col:
                if not board_used[x][y] and wd[0] == board[x][y]:
                    board_used[x][y] = 1
                    if search_path(x+1, y, wd[1:]) or search_path(x-1, y, wd[1:]) or search_path(x, y+1, wd[1:])\
                            or search_path(x, y-1, wd[1:]):
                        return True
                    board_used[x][y] = 0
            return False

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if search_path(i, j, word):
                        return True
        return False
