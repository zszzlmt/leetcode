class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for idx in range(1, len(s2) + 1):
            dp[0][idx] = dp[0][idx - 1] + ord(s2[idx - 1])
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
            for j in range(1, len(s2) + 1):
                if s2[j - 1] == s1[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1] + ord(s2[j - 1]),
                                   dp[i - 1][j] + ord(s1[i - 1]))
        return dp[len(s1)][len(s2)]
