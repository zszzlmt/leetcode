class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return list()
        res = [[1]]
        for row in range(1, numRows):
            tmp = list()
            for idx in range(row + 1):
                if idx == 0 or idx == row:
                    tmp.append(1)
                else:
                    tmp.append(res[row - 1][idx - 1] + res[row - 1][idx])
            res.append(tmp)
        return res