# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         def is_adj(u: str, v: str):
#             cnt  = 0
#             for u_c, v_c in zip(u, v):
#                 if u_c != v_c:
#                     cnt += 1
#             return True if cnt == 1 else False
        
#         n = len(wordList)
#         visited = [0 for i in range(n)]
#         track = {}
#         queue = [beginWord]
#         track[beginWord] = [[beginWord]]
        
#         while len(queue) > 0:
#             u = queue[0]
#             del queue[0]
#             for v_idx, v in enumerate(wordList):
#                 if visited[v_idx] == 0 and is_adj(u, v):
#                     queue.append(v)
#                     visited[v_idx] = True
#                     track[v] = track[u] + v 
#         res = []
#         u = endWord
#         if u not in track:
#             return []
#         while u != beginWord:
#             print(u)
#             res.append(str(u))
#             u = track[u]
#         res.append(str(beginWord))

#         return [res[::-1]]
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not endWord or not beginWord or not wordList or endWord not in wordList \
            or beginWord == endWord:
            return []

        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Build graph, bi-BFS
        # ans = []
        bqueue = collections.deque()
        bqueue.append(beginWord)
        equeue = collections.deque()
        equeue.append(endWord)
        bvisited = set([beginWord])
        evisited = set([endWord])
        rev = False 
        #graph
        parents = collections.defaultdict(set)
        found = False 
        depth = 0
        while bqueue and not found:
            depth += 1 
            length = len(bqueue)
            # print(queue)
            localVisited = set()
            for _ in range(length):
                word = bqueue.popleft()
                for i in range(L):
                    for nextWord in all_combo_dict[word[:i] + "*" + word[i+1:]]:
                        if nextWord == word:
                            continue
                        if nextWord not in bvisited:
                            if not rev:
                                parents[nextWord].add(word)
                            else:
                                parents[word].add(nextWord)
                            if nextWord in evisited:    
                                found = True
                            localVisited.add(nextWord)
                            bqueue.append(nextWord)
            bvisited = bvisited.union(localVisited)
            bqueue, bvisited, equeue, evisited, rev = equeue, evisited, bqueue, bvisited, not rev
        # print(parents)
        # print(depth)
        # Search path, DFS
        ans = []
        def dfs(node, path, d):
            if d == 0:
                if path[-1] == beginWord:
                    ans.append(path[::-1])
                return 
            for parent in parents[node]:
                path.append(parent)
                dfs(parent, path, d-1)
                path.pop()
        dfs(endWord, [endWord], depth)
        return ans
