class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        n = len(nums)
        
        for i in range(n):
            if target - nums[i] in indices:
                return [indices[target-nums[i]], i]
            indices[nums[i]] = i
        return [0, 0]
