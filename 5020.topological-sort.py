from collections import deque
class Solution:
    def topoSort_DFS(self, V, adj):
        def dfs(node):
            vis[node] = 1
            for it in adj[node]:
                if not vis[it]:
                    dfs(it)
            stack.append(node)

        vis = [0]*0
        stack = []
        for i in range(V):
            if not vis[i]:
                dfs(node)
        ans = []
        while stack:
            ans.append(stack.pop())
        return ans
    
    def topoSort_BFS(self, V, adj):
        # precomp
        indeg = [0]*V           # indegrees of each V
        for i in range(V):
            for it in adj[i]:
                indeg[it] += 1
        
        q = deque()             # enque all 0 inDegree nodes
        for node in range(V):
            if indeg[node] == 0:
                q.append(node)
        
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)    # save topo order

            for it in adj[node]:
                indeg[it] -= 1
                if indeg[it] == 0:
                    q.append(it)
        
        return ans
