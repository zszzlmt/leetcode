from collections import defaultdict


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in points:
            dist = defaultdict(0)
            for j in points:
                dist[pow(i[0] - j[0], 2) + pow(i[1] - j[1], 2)] += 1
            for _, times in dist.items():
                res += times * (times - 1)
        return res
