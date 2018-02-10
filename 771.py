class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if len(J) == 0 or len(S) == 0:
            return 0
        res = 0
        for item in J:
            res += S.count(item)
        return res