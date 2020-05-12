class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        l = len(timeSeries)
        if l == 0:
            return 0
        if l == 1:
            return duration
        res = duration
        for idx in range(l - 1):
            if timeSeries[idx + 1] - timeSeries[idx] >= duration:
                res += duration
            else:
                res += timeSeries[idx + 1] - timeSeries[idx]
        return res

