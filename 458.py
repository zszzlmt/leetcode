import math


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        try:
            return int(math.ceil(math.log(buckets, minutesToTest // minutesToDie + 1)))
        except ZeroDivisionError as _:
            return 0
