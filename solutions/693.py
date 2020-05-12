class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = bin(n)[2:]
        if len(s) == 1:
            return True
        elif len(s) == 2:
            if s[0] != s[-1]:
                return True
            else:
                return False
        tmp = [0 if s[idx] != s[idx - 1] and s[idx] != s[idx + 1] else 1 for idx in range(1, len(s) - 1) ]
        if not sum(tmp):
            return True
        else:
            return False