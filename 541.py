class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        pos = 0
        need = 2 * k
        res = str()
        while True:
            if len(s[pos:]) >= need:
                res += s[pos:pos + k][::-1]
                res += s[pos + k:pos + need]
                pos += need
            else:
                if len(s[pos:]) < k:
                    res += s[pos:][::-1]
                else:
                    res += s[pos:pos + k][::-1]
                    res += s[pos + k:]
                break
        return res