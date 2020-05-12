class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter

        c = Counter(nums).most_common()
        res = list()
        for idx in range(k):
            res.append(c[idx][0])
        return res
