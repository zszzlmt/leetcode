class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)
        while True:
            m = (l + r) // 2
            if m == 0 or m == len(nums) - 1:
                return nums[m]
            if nums[m] != nums[m - 1] and nums[m] != nums[m + 1]:
                return nums[m]
            else:
                if nums[m] == nums[m - 1]:
                    if m % 2 == 1:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if m % 2 == 1:
                        r = m - 1
                    else:
                        l = m + 1
