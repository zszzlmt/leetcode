class Solution(object):

    res = None
    alpha = None

    def __permutation__(self, s, idx_alpha):
        if idx_alpha >= len(self.alpha):
            return
        idx = self.alpha[idx_alpha]
        self.res.append(s)
        self.__permutation__(s, idx_alpha + 1)
        if idx != len(s) - 1:
            if s[idx].islower():
                t = s[:idx] + s[idx].upper() + s[idx + 1:]
                self.res.append(t)
                self.__permutation__(t, idx_alpha + 1)
            else:
                t = s[:idx] + s[idx].lower() + s[idx + 1:]
                self.res.append(t)
                self.__permutation__(t, idx_alpha + 1)
        else:
            if s[idx].islower():
                t = s[:idx] + s[idx].upper()
                self.res.append(t)
                self.__permutation__(t, idx_alpha + 1)
            else:
                t = s[:idx] + s[idx].lower()
                self.res.append(t)
                self.__permutation__(t, idx_alpha + 1)

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not len(S):
            return list()
        self.alpha = list()
        for idx in range(len(S)):
            if S[idx].isalpha():
                self.alpha.append(idx)
        if not len(self.alpha):
            return [S]
        self.res = list()
        self.__permutation__(S, 0)
        return list(set(self.res))