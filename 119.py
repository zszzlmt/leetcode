class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for row_idx in range(rowIndex):
            res = [x + y for x, y in zip([0] + res, res + [0])]
        return res
