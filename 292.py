class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        if n % 4 == 0:
            return False
        return True