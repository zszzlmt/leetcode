class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('A') > 1:
            return False
        for idx in range(len(s) - 2):
            if s[idx] == 'L' and s[idx + 1] == 'L' and s[idx + 2] == 'L':
                return False
        return True