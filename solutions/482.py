class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        c = ''.join(S.split('-'))
        c = ''.join([c[idx].upper() if c[idx].isalpha() else c[idx] for idx in range(len(c))])
        if len(c) <= K:
            return c
        res = str()
        head_l = len(c) % K
        if head_l:
            res += c[:head_l]
            c = c[head_l:]
        while len(c):
            res += '-' + c[:K]
            c = c[K:]
        if not head_l:
            res = res[1:]
        return res
