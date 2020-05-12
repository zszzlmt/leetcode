class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        valid = []
        res = 0
        base = 10
        sign = []
        num_flag = 0
        for idx in range(len(str)):
            c = str[idx]
            if c == ' ':
                if len(valid) != 0 or num_flag == 1 or len(sign) != 0:
                    break
                continue
            if (c == '-' or c == '+') and len(valid) == 0:
                if len(sign) != 0:
                    return 0
                sign.append(c)
            elif c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                num_flag = 1
                if c == '0' and len(valid) == 0:
                    continue
                valid.append(c)
            else:
                break
        for idx in range(len(valid)):
            res *= base
            res += int(valid[idx])
        if len(sign) != 0 and sign[0] == '-':
            res *= (-1)
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        if res < - (2 ** 31):
            res = - (2 ** 31)
        return res