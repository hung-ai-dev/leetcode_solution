class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n, i, j, s, shortest = len(nums), 0, 0, 0, len(nums)+1
        while j < n:
            s += nums[j]
            print(i, j, n, s, s - nums[i], target)
            while (s - nums[i]) >= target:
                s -= nums[i]
                i += 1
            if s >= target:
                shortest = min(shortest, j - i + 1)
            j += 1
        return 0 if shortest==len(nums)+1 else shortest
