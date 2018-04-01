class Solution(object):

    rows = None
    cols = None
    board = None

    def check(self, r, c):
        if (r == 0 or self.board[r - 1][c] == '.') and (c == 0 or self.board[r][c - 1] == '.'):
            return True
        return False

    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        cnt = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if board[r][c] == 'X' and self.check(r, c):
                    cnt += 1
        return cnt
