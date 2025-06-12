class Solution:
    def shortestPath(self, N, M, edges):
        # making adj
        adj = [[] for _ in range(N)]
        for n1, n2, wt in edges:
            adj[n1].append((n2, wt))

        # get the topological stack
        topoStack = self.topologicalSort(N, adj)

        # distance list
        dist = [1e9] * N
        dist[0] = 0         # src node distance marked as 0

        # relax the edges
        while topoStack:
            node = topoStack.pop()
            for it, wt in adj[node]:

                # if the dist from node to it less, update dist
                if dist[node] + wt < dist[it]:
                    dist[it] = dist[node] + wt
        
        # make unreachable nodes distance -1
        for i in range(N):
            if dist[i] == 1e9:
                dist[i] = -1
        
        # return results
        return dist
    
    
    def topologicalSort(self, V, adj):
        def dfs(node):
            vis[node] = 1
            for it,_ in adj[node]:
                if not vis[it]:
                    dfs(it)
            
            topoStack.append(node)
            return 
        
        vis = [0]*V
        topoStack = []

        for i in range(V):
            if not vis[i]:
                dfs(i)
        
        return topoStack