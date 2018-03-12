class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = bin(num)
        res = '0b'
        for i in tmp[2:]:
            res += str(1 - int(i))
        return int(res, 2)