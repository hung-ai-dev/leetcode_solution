class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = sorted(arr)
        n = len(arr)
        res = 0
        mod = 1e9 + 7
        mapper = {val: idx for idx, val in enumerate(arr)}
        dp = [1 for i in range(n)]
        
        for i, val_p in enumerate(arr):
            for j, val_l in enumerate(arr[:i]):
                val_r = val_p // val_l
                if val_p % val_l == 0 and val_r in mapper:
                    dp[i] = (dp[i] + dp[mapper[val_l]]*dp[mapper[val_r]]) % mod
            res = (res + dp[i]) % mod
        return int(res)
