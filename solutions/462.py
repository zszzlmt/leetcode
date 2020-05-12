class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pivot = sorted(nums)[len(nums) // 2]
        return sum([abs(num - pivot) for num in nums])
