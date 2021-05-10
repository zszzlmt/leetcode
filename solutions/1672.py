class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        if len(accounts) == 0:
            return 0
        return max([sum(values) for values in accounts])