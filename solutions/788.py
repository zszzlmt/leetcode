class Solution(object):

    def __check__(self, n):
        flag = False
        while n:
            tmp = n % 10
            n /= 10
            if tmp in [0, 1, 2, 5, 6, 8, 9]:
                if tmp in [2, 5, 6, 9]:
                    flag = True
            else:
                return False
        return flag

    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        for num in range(1, N + 1):
            if self.__check__(num):
                res += 1
        return res
