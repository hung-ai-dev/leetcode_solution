class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(2**len(nums)):
            sub = []
            bi = format(i, "b").zfill(len(nums))
            for idx, val in enumerate(bi):
                if val == "1":
                    sub.append(nums[idx])
            res.append(sub)
        return res
