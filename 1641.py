class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0, 0, 0, 0, 0] for i in range(n)]
        for i in range(5):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(5):
                for k in range(j+1):
                    dp[i][j] += dp[i-1][k]
        print(dp)
        s = 0
        for i in range(5):
            s += dp[n-1][i]
        return s
