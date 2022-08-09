class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Use deque to store descending value and corresponding index of nums in the sliding window.
        The maximum value of sliding window is head of deque.
        '''
        stack = []
        res = []
        for i, val in enumerate(nums):
            while len(stack) > 0 and val > stack[-1][0]:
                stack.pop()
            stack.append([val, i])
            if stack[0][1] <= i-k:
                del stack[0]
            if i >= k-1:
                res.append(stack[0][0])
        return res
