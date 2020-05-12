class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = str.split(' ')
        l = len(s)
        if len(pattern) == 0 and l == 0:
            return True
        if len(pattern) == 0 or l == 0:
            return False
        if len(pattern) != l:
            return False
        d1 = dict()
        d2 = dict()
        for idx in range(l):
            if pattern[idx] not in d1:
                d1[pattern[idx]] = s[idx]
            if s[idx] not in d2:
                d2[s[idx]] = pattern[idx]
            if d1[pattern[idx]] != s[idx] or d2[s[idx]] != pattern[idx]:
                return False
        return True
