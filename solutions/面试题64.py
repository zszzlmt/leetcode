class Solution(object):

    result = 0

    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        n > 1 and self.sumNums(n-1)
        self.result += n
        return self.result
