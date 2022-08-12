class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def generator(res: list, n: int, k: int, cur: list, idx: int):
            if idx == k:
                print(cur, idx)
                res.append(cur[1:])
                return
            
            for val in range(cur[idx]+1, n+1, 1):
                cur[idx+1] = val
                generator(res, n, k, cur, idx+1)
            
        res = []
        cur = [0 for i in range(k+1)]
        generator(res, n, k, cur, 0)
        return res
