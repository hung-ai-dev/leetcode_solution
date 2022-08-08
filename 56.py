class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = [intervals[0]]
        for inter in intervals:
            if inter[0] > res[-1][1]:
                res.append(inter)
            else:
                res[-1][1] = max(inter[1], res[-1][1])
        return res
