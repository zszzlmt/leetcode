class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = max(nums)
        idx = nums.index(m1)
        nums.remove(m1)
        if len(nums):
            m2 = max(nums)
        else:
            return 0
        if m1 >= m2 * 2:
            return idx
        return -1
