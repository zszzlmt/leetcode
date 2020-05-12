import copy


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if nums1 == [0] and m == 0 and nums2 == [1] and n == 1:
            nums1[0] = 1
            return
        cnt = 0
        idx = 0
        res = nums1
        nums1 = copy.deepcopy(nums1[:m])
        nums2 = copy.deepcopy(nums2[:n])
        while True:
            if idx == n:
                while cnt < m:
                    nums1.append(nums1.pop(0))
                    cnt += 1
                break
            if cnt == m:
                nums1.append(nums2[idx])
                idx += 1
                continue
            elif nums2[idx] <= nums1[0]:
                nums1.append(nums2[idx])
                idx += 1
                continue
            else:
                nums1.append(nums1.pop(0))
                cnt += 1
        pos = 0
        for item in nums1:
            if pos < len(res):
                res[pos] = item
                pos += 1
            else:
                res.append(item)