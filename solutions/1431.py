class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = list()
        max_now = max(candies)
        for candies_num in candies:
            if max_now - candies_num <= extraCandies:
                result.append(True)
            else:
                result.append(False)

        return result