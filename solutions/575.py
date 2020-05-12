class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        l = len(candies) // 2
        k = len(set(candies))
        if k > l:
            return l
        else:
            return k
        