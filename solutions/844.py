class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        idx_s = len(S) - 1
        idx_t = len(T) - 1
        while True:
            cnt_s = 0
            while cnt_s != 0 or S[idx_s] == '#':
                if idx_s < 0:
                    break
                if S[idx_s] == '#':
                    idx_s -= 1
                    cnt_s += 1
                else:
                    idx_s -= 1
                    cnt_s -= 1

            cnt_t = 0
            while cnt_t != 0 or T[idx_t] == '#':
                if idx_t < 0:
                    break
                if T[idx_t] == '#':
                    idx_t -= 1
                    cnt_t += 1
                else:
                    idx_t -= 1
                    cnt_t -= 1

            if idx_s < 0 or idx_t < 0:
                if idx_s >= 0 or idx_t >= 0:
                    return False
                return True

            if S[idx_s] != T[idx_t]:
                return False

            idx_s -= 1
            idx_t -= 1