class Solution(object):
    
    def __check__(self, n):
        digits = list()
        tmp = n
        while tmp != 0:
            digits.append(tmp % 10)
            tmp = tmp // 10
            if digits[-1] == 0:
                return False
        for digit in digits:
            if n % digit != 0:
                return False
        return True
    
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right + 1):
            if self.__check__(num):
                res.append(num)
        return res