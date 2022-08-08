class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        x_height = sorted(heights)
        cnt = 0 
        for x, y in zip(x_height, heights):
            cnt += 1 if x != y else 0
        return cnt
