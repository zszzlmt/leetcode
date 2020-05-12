class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        c = 0
        for idxx in range(1, l + 1):
            idx = l - idxx
            if idxx == 1:
                tmp = digits[idx] + 1 + c
            else:
                tmp = digits[idx] + c
            c = tmp // 10
            digits[idx] = tmp % 10
        if c != 0:
            digits.insert(0, 1)
        return digits