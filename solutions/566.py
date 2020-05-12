class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        table = list()
        for row in nums:
            table += row
        if len(table) != r * c:
            return nums
        res = list()
        idx = 0
        for row in range(r):
            tmp_row = list()
            for col in range(c):
                tmp_row.append(table[idx])
                idx += 1
            res.append(tmp_row)
        return res