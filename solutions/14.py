class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l = len(strs)
        if l == 0:
            return ''
        if l == 1:
            return strs[0]
        while True:
            com = strs[0]
            for idx in range(len(com)):
                for s in strs[1:l]:
                    if len(s) - 1 < idx or s[idx] != com[idx]:
                        return com[:idx]
            return com