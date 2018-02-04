class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0
        flag = 0
        res = 0
        for idxx in range(1, l + 1):
            idx = l - idxx
            if flag == 0:
                if s[idx] != ' ':
                    flag = 1
                    res += 1
                else:
                    continue
            else:
                if s[idx] != ' ':
                    res += 1
                else:
                    break
        if flag == 0:
            return 0
        else:
            return res