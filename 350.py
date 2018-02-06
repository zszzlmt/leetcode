class Solution(object):
    def intersect(self, nums1, nums2):
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
        resd = dict()
        for idx in range(l1):
            if nums1[idx] not in d:
                d[nums1[idx]] = 1
            else:
                d[nums1[idx]] += 1
        for idx in range(l2):
            if nums2[idx] in d:
                if nums2[idx] not in resd:
                    res.append(nums2[idx])
                    resd[nums2[idx]] = 1
                elif resd[nums2[idx]] < d[nums2[idx]]:
                    res.append(nums2[idx])
                    resd[nums2[idx]] += 1
        return res
