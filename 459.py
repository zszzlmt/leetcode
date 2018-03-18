class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(set(s)) == 1 and len(s) > 1:
            return True
        l = len(s)
        max_size = l // 2 + 1
        for times in range(2, max_size):
            if l % times != 0:
                continue
            size = l / times
            for i in range(times - 1):
                if s[i * size:(i + 1) * size] != s[(i + 1) * size:(i + 2) * size]:
                    break
            else:
                return True
        return False