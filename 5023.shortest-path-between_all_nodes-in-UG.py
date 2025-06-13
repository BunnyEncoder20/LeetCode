class Solution:
    def shortestPath(self, edges, N, M):
        # make adj list 
        adj = [[] for _ in range(N)]
        for n1,n2 in edges:
            adj[n1].append(n2)          # cause undirected graph
            adj[n2].append(n1)          # we append each to other's adj
        
        # distance list and mark src at dist 0
        dist = [float('inf')] * N
        dist[0] = 0

        # queue for bfs
        q = deque([0])

        # traverse the graph
        while q:
            node = q.popleft()
            for it in adj[node]:
                if dist[node] + 1 < dist[it]:
                    dist[it] = dist[node] + 1       # save shorter dist of it
                    q.append(it)                    # enque it
        
        # mark dist = -1 for unreachable nodes
        for i in range(N):
            if dist[i] == float('inf'):
                dist[i] = -1

        return dist