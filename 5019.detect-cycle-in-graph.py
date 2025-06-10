from collections import deque
class Solution:
    def isCycle(self, V, adj) -> bool:
        
        def detectCycle_bfs(src) -> bool:
            q = deque([
                (src, -1)
            ])
            vis[src] = 1
            
            while q:
                node, parent = q.popleft()
                for it in adj[node]:
                    if not vis[it]:
                        vis[it] = 1             # mark
                        q.append((it, node))    # enque

                    # if visited but not parent node
                    elif parent != it:
                        return True     # cycle detected
            
            return False


        def detectCycle_dfs(node, parent) -> bool:
            vis[node] = 1        # mark
            
            for it in adj[node]:
                if not vis[it]:
                    # recursively dfs
                    # if cycle detected deeper, return that
                    if detectCycle_dfs(it, node):   
                        return True
                elif parent != it:
                    return True     # cycle detected
            
            return False

        vis = [0]*V
        isCycle = False
        for i in range(V):
            if not vis[i]:
                # Use one of the traversals
                # if detectCycle_bfs(i): return True
                if detectCycle_dfs(i, -1): return True

        
