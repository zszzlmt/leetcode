class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False for _ in range(N + 1)]
        for idx in range(1, len(dp)):
            for idxx in range(1, idx//2+1):
                if idx % idxx == 0 and dp[idx-idxx] == False:
                    dp[idx] = True
                    break
        return dp[N]
