class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        l, longest = 0, 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > 1:
                l += 1
            if nums[r] - nums[l] == 1:
                longest = max(longest, r-l+1)
        return longest
