from collections import defaultdict


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = defaultdict(list)
        for idx in range(len(nums)):
            d[nums[idx]].append(idx)
        for _, values in d.items():
            for idx in range(1, len(values)):
                if values[idx] - values[idx - 1] <= k:
                    return True
        return False
