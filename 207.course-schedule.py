#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # init
        V = numCourses
        adj = [[] for _ in range(V)]
        indeg = [0] * V
        for a,b in prerequisites:
            adj[b].append(a)
            indeg[a] += 1
        
        # init topo
        q = deque([node for node in range(V) if indeg[node] == 0])
        topo = []
        
        # BFS
        while q:
            node = q.popleft()
            topo.append(node)
            for it in adj[node]:
                indeg[it] -= 1
                if indeg[it] == 0:
                    q.append(it)
        
        return len(topo) == V
        
        
# @lc code=end

