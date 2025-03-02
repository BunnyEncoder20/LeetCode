#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(root):
            q = deque([root])
            colored[root] = False
            while q:
                node = q.popleft()
                for it in graph[node]:
                    if not colored[it]:
                        colored[it] = not colored[node]
                        q.append(it)
                    elif colored[it] == colored[node]:
                        return False
            return True
        
        colored = [None]*len(graph)
        for i in range(len(graph)):
            if not colored[i]:
                completed = bfs(i)
                if not completed: return False
        return True
                
        
        
# @lc code=end

