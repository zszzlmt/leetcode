class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        nums = sorted([abs(num) for num in A])
        return [pow(num, 2) for num in nums]
