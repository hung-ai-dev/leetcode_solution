class Solution:
    def trarvese(self, node: int, n: int, edges: list):
        dis = [-1 for i in range(n)]
        dis[node] = 0
        while edges[node] != -1 and dis[edges[node]] == -1:
            next_n = edges[node]
            dis[next_n] = dis[node] + 1
            node = next_n
        return dis
        
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dis_1 = self.trarvese(node1, n, edges)
        dis_2 = self.trarvese(node2, n, edges)
        dis_3 = [max(a, b) if a > -1 and b > -1 else 1e6 for a, b in zip(dis_1, dis_2)]
        print(dis_1, dis_2, dis_3)
        min_idx, min_val = -1, 1e6
        for i in range(n):
            if dis_3[i] < min_val:
                min_idx = i
                min_val = dis_3[i]
        return min_idx
