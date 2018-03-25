class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = list()
        res = 0
        for op in ops:
            if op == '+':
                points.append(points[-1] + points[-2])
                res += points[-1]
                continue
            if op == 'D':
                points.append(points[-1] * 2)
                res += points[-1]
                continue
            if op == 'C':
                res -= points[-1]
                points.pop()
                continue
            points.append(int(op))
            res += int(op)
        return res
