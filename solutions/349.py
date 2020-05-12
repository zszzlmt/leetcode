class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = dict()
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 == 0 or l2 == 0:
            return []
        res = list()
        for idx in range(l1):
            if nums1[idx] not in d:
                d[nums1[idx]] = 1
        for idx in range(l2):
            if nums2[idx] in d and nums2[idx] not in res:
                res.append(nums2[idx])
        return res