import bisect
from collections import Counter

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = Counter(numbers)
        for item in numbers:
            to_find = target - item
            pos = bisect.bisect_left(numbers, to_find)
            if pos < len(numbers) and numbers[pos] == to_find:
                if item != to_find:
                    return [numbers.index(item) + 1, pos + 1]
                elif  count[to_find] > 1:
                    return [numbers.index(item) + 1, numbers.index(item) + 2]
