class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num

        pivot = xor & -xor

        a = 0
        b = 0
        for num in nums:
            if num & pivot:
                a ^= num
            else:
                b ^= num
        return [a, b]
