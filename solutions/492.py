import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if area == 1:
            return [1, 1]
        min_dist = None
        res = None
        for w in range(1, int(math.sqrt(area)) + 1):
            if area % w == 0:
                l = area / w
                if l >= w and (min_dist is None or min_dist > l - w):
                    min_dist = l - w
                    res = [l, w]
        return res
