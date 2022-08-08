class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        n = len(heights)
        res = [0 for i in range(n)]
        
        for i in range(n-1,-1,-1):
            h = heights[i]
            cnt = 0
            while len(stack) > 0 and stack[-1][0] < h:
                stack.pop()
                cnt += 1
            if len(stack) > 0:
                cnt += 1
            stack.append([h, i])
            res[i] = cnt
        return res
