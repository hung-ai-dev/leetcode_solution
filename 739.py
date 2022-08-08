class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)        
        loc = [1e6 for i in range(102)]
        min_loc = [1e6 for i in range(102)]
        res = [0 for i in range(n)]
        stack = []
        
        for i in range(n-1,-1,-1):
            temp = temperatures[i]
            while len(stack) > 0 and stack[-1][0] <= temp:
                stack.pop()
            if len(stack) > 0:
                res[i] = stack[-1][1] - i
            else:
                res[i] = 0
            stack.append([temp, i])
        return res
