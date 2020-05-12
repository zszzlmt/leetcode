class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        xcnt = 0
        ocnt = 0
        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    xcnt += 1
                elif board[row][col] == 'O':
                    ocnt += 1
        if not(xcnt == ocnt or xcnt == ocnt + 1):
            return False

        xline = 0
        oline = 0
        for row in range(3):
            same = True
            for col in range(3):
                if col == 0:
                    tar = board[row][col]
                else:
                    if board[row][col] != tar:
                        same = False
                        break
            if same:
                if tar == 'X':
                    xline += 1
                elif tar == 'O':
                    oline += 1

        for col in range(3):
            same = True
            for row in range(3):
                if row == 0:
                    tar = board[row][col]
                else:
                    if board[row][col] != tar:
                        same = False
                        break
            if same:
                if tar == 'X':
                    xline += 1
                elif tar == 'O':
                    oline += 1

        same = True
        for idx in range(3):
            if idx == 0:
                tar = board[idx][idx]
            else:
                if board[idx][idx] != tar:
                    same = False
                    break
        if same:
            if tar == 'X':
                xline += 1
            elif tar == 'O':
                oline += 1

        same = True
        for idx in range(3):
            if idx == 0:
                tar = board[idx][2 - idx]
            else:
                if board[idx][2 - idx] != tar:
                    same = False
                    break
        if same:
            if tar == 'X':
                xline += 1
            elif tar == 'O':
                oline += 1

        if xline and oline:
            return False
        if xline:
            if not (xcnt == ocnt + 1):
                return False
        if oline:
            if not (xcnt == ocnt):
                return False
        return True
