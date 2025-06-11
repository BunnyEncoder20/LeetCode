#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from collections import deque
class Solution:
    def isBipartite(self, adj: List[List[int]]) -> bool:
        def dfs(node, prevNodeColor):
            colored[node] = -1*prevNodeColor    # mark opp color
            for it in adj[node]:
                if not colored[it]:
                    flag = dfs(it, colored[node])
                    
                    # if false from futher in traversal, return it
                    if not flag: return False
                
                # the node was already colored
                elif colored[it] == colored[node]:
                    return False
            
            return True
            

        def bfs(snode,scolor):
            q = deque([(snode, scolor)])

            while q:
                node, color = q.popleft()
                for it in adj[node]:
                    # If not colored
                    if not colored[it]:
                        colored[it] = -1*color      # color opposite of parent node color
                        q.append((it, -1*color))    # enque adj node

                    # If colored same color as parent node
                    elif colored[it] == color:
                        return False
            
            # traverse the graph, didn't flag false
            return True

        V = len(adj)
        colored = [0]*V  # will color 1 and -1

        for node in range(V):
            if not colored[node]:
                completely_biparted = dfs(node, 1)
                # completely_biparted = bfs(node, 1)

                # Return false if any part of the graph
                # was not able to be biparted
                if not completely_biparted:
                    return False
        
        # Entire graph was parted into 2 completely
        return True
        
# @lc code=end

