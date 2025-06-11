from collections import deque
class Solution:
    def isCyclic_DFS(self, V, adj):
        def dfs(node):
            # mark node
            vis[node] = 1
            pathvis[node] = 1

            for it in adj[node]:

                # if node was in this path, cycle found
                if pathvis[it]:
                    return True

                # if node not visited, dfs further
                elif not vis[it]:
                    # if cycle found further down dfs
                    if dfs(it): return True
            
            # node already visted / no cycle found
            pathvis[node] = 0       # unmark path visited
            return False
                    

        vis = [0]*V
        pathvis = [0]*V

        for i in range(V):
            if not vis[i]:
                isCycle = dfs(i)
                if isCycle:
                    return True
        
        # no cycles could be found
        return False




    def isCyclic_BFS(self, V, adj):
        # precomp: Find indegs
        indeg = [0]*V
        for i in range(V):
            for it in adj[i]:
                indeg[it] += 1
        
        # enque nodes with indeg = 0
        q = deque([node for node,indegree in enumerate(indeg) if indegree == 0])

        # perform Topological sort
        topological_order = []
        while q:
            node = q.popleft()
            topological_order.append(node)
            for it in adj[node]:
                indeg[it] -= 1
                if indeg[it] == 0:
                    q.append(it)
        
        # if the topological order has all the nodes, then it's a DAG
        # Else if the num of nodes are less, the topo missed nodes cause of cycle 
        return True if len(topological_order) < V else False

