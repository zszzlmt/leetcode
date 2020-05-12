from collections import Counter


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        return [sum([idx if count[idx] == 2 else 0 for idx in range(1, len(nums) + 1)]),
               sum([idx if idx not in count else 0 for idx in range(1, len(nums) + 1)])]
