#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from typing import List
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


        def bfs(root):
            q = deque([root])
            colored[root] = 1
            while q:
                node = q.popleft()
                for nn in adj[node]:
                    if not colored[nn]:
                        colored[nn] = -1 * colored[node]    # color opposite of neighbour node
                        q.append(nn)                        # put into q for processing
                    elif colored[nn] == colored[node]:      # if neighbour colored same as node
                        return False
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
