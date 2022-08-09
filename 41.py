class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        1. because array has n elements, so the smallest missing interger must be <= n+1
        2. let's think the array as linked list, hence traverse and mark the array
        '''
        nums = [0] + nums

        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] >= n:
                nums[i] = 0

        for i in range(1, n, 1):
            j = nums[i]
            if nums[i]==i or nums[i]==0:
                continue
            while True:
                temp = nums[j]
                nums[j] = j
                j = temp
                if j == 0 or j == nums[j]:
                    break
                    
        for i in range(1, n, 1):
            if i != nums[i]:
                return i
        return n
