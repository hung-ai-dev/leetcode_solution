class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        score = [0 for i in range(n)]
        
        for u in range(n):
            score[edges[u]] += u
        idx = 0
        # print(score)
        for i, v in enumerate(score):
            if v > score[idx]:
                idx = i
        return idx
