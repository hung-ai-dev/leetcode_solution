class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(2**len(nums)):
            sub = []
            bi = format(i, "b").zfill(len(nums))
            for idx, val in enumerate(bi):
                if val == "1":
                    sub.append(nums[idx])
            res.append(sub)
            
        res.sort()
        final = [[]]
        for val in res[1:]:
            if val != final[-1]:
                final.append(val)
        return final
