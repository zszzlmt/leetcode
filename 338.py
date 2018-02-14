class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        while len(res) <= num + 1:
            res += [i + 1 for i in res]
        return res[:num + 1]
