class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        queue = [0]
        visited = [0 for i in range(n)]
        visited[0] = 1
        for v in restricted:
            visited[v] = 1
        dict_e = {}
        for e in edges:
            if e[0] not in dict_e:
                dict_e[e[0]] = [e[1]]
            else:
                dict_e[e[0]].append(e[1])

            if e[1] not in dict_e:
                dict_e[e[1]] = [e[0]]
            else:
                dict_e[e[1]].append(e[0])

        cnt, l = 0, 0
        while l < len(queue):
            node = queue[l]
            l += 1
            print(node)
            for next_node in dict_e[node]:
                if visited[next_node] == 0:
                    queue.append(next_node)
                    visited[next_node] = 1
        return len(queue)
                
                
