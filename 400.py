class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = ''.join([str(n) for n in range(2 ** 31)])
        return table[n]
