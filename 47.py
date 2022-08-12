class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def traverse(nums: list, visited :list, res: list, cur: list, cur_idx: int):
            if cur_idx == len(nums):
                if cur[:] not in res:
                    res.append(cur[:])
                return
            
            for idx, val in enumerate(nums):
                if not visited[idx]:
                    visited[idx] = True
                    cur[cur_idx] = val
                    traverse(nums, visited, res, cur, cur_idx+1)
                    visited[idx] = False
        nums.sort()
        res = []
        visited = [False for i in range(len(nums))]
        cur = [0 for i in range(len(nums))]
        traverse(nums, visited, res, cur, 0)
        # res.sort()
        
        return res
