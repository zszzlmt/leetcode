import bisect


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        if len(heaters) == 1:
            return max(abs(houses[0] - heaters[0]), abs(houses[-1] - heaters[0]))
        div = [(heaters[idx] + heaters[idx + 1]) / 2 for idx in range(len(heaters) - 1)]
        parts = [[] for _ in range(len(heaters))]
        for idx in range(len(houses)):
            parts[bisect.bisect_left(div, houses[idx])].append(houses[idx])
        max_dist = 0
        for idx in range(len(parts)):
            hs = parts[idx]
            if not len(hs):
                continue
            dist = max(abs(hs[0] - heaters[idx]), abs(hs[-1] - heaters[idx]))
            if dist > max_dist:
                max_dist = dist
        return max_dist