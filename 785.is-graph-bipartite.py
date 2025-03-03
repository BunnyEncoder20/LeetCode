#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node, node_color):
            colored[node] = node_color
            for it in graph[node]:
                if not colored[it]:
                    if not dfs(it, not node_color):
                        return False
                elif colored[it] == node_color:
                    return False 
            return True
        
        colored = [None]*len(graph)
        for i in range(len(graph)):
            if not colored[i]:
                completed = dfs(i, False)
                if not completed: return False
        return True
                
        
        
# @lc code=end

