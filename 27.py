class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        l = len(nums)
        cnt = 0
        fpos = l - 1
        tpos = 0
        while fpos >= 0 and nums[fpos] == val:
            fpos -= 1
        while tpos < l and nums[tpos] != val:
            tpos += 1
        for idx in range(l):
            if nums[idx] == val:
                cnt += 1
        while tpos < fpos:
            nums[tpos] = nums[fpos]
            nums[fpos] = val
            while fpos >= 0 and nums[fpos] == val:
                fpos -= 1
            while tpos < l and nums[tpos] != val:
                tpos += 1
        return l - cnt