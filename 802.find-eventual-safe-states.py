#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

# @lc code=start
from collections import deque
class Solution:
    def eventualSafeNodes_dfs(self, adj: List[List[int]]) -> List[int]:
        def dfs(node):
            # mark
            vis[node] = 1
            pathvis[node] = 1

            for it in adj[node]:
                # if the node is in path,
                # cycle detected
                if pathvis[it]:
                    return True

                # if the not path and vis, dfs further
                elif not vis[it]:

                    # if cycle found further down
                    if dfs(it):
                        return True
            
            # No cycle found, so mark as safe node
            pathvis[node] = 0
            isSafe[node] = 1
            return False


        # constants 
        V = len(adj)
        vis = [0]*V
        pathvis = [0]*V
        isSafe = [0]*V

        # traverse
        for i in range(V):
            if not vis[i]:
                dfs(i)
        
        # construct ans
        ans = [node for node in range(V) if isSafe[node]]

        return ans

    def eventualSafeNodes(self, adj: List[List[int]]) -> List[int]:
        
        def topologicalSort():
            # make indegree list 
            indeg = [0]*V 
            for n in range(V):
                for it in revAdj[n]:
                    indeg[it] += 1
            
            # enque nodes with indeg = 0
            q = deque(n for n in range(V) if indeg[n]==0)

            # toposort
            toposort = []
            while q:
                node = q.popleft()
                toposort.append(node)
                for it in revAdj[node]:
                    indeg[it] -= 1
                    if indeg[it] == 0:
                        q.append(it)
            
            return toposort


        # reverse graph; Make revAdj list
        V = len(adj)
        revAdj = [[] for _ in range(V)]
        for i in range(V):
            for it in adj[i]:
                revAdj[it].append(i)
        
        # Toposort
        safeNodes = topologicalSort()
        safeNodes.sort()
        return safeNodes


# @lc code=end

