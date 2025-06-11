#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

# @lc code=start
class Solution:
    def eventualSafeNodes(self, adj: List[List[int]]) -> List[int]:
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
            isSafe[node] = 1
            pathvis[node] = 0
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
        
# @lc code=end

