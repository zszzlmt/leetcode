class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l = max(len(num1), len(num2))
        res = str()
        base = ord('0')
        c = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for idx in range(l):
            if idx < len(num1):
                n_1 = num1[idx]
            else:
                n_1 = '0'
            if idx < len(num2):
                n_2 = num2[idx]
            else:
                n_2 = '0'
            tmp = ord(n_1) - base + ord(n_2) - base + c
            if tmp >= 10:
                tmp %= 10
                c = 1
            else:
                c = 0
            res += chr(tmp + base)
        if c:
            res += '1'
        return res[::-1]