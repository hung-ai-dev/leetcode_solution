class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1, n, 1):
            for j in range(i, 0, -1):
                if nums[j] < nums[j-1]:
                    tmp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = tmp
                else:
                    break
        
