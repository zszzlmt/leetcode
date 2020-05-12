class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        res = str()
        neg_flag = False
        if num < 0:
            neg_flag = True
            num = abs(num)
        num, tmp = divmod(num, 7)
        res += str(tmp)
        while num:
            num, tmp = divmod(num, 7)
            res += str(tmp)
        if neg_flag:
            return '-' + res[::-1]
        else:
            return res[::-1]