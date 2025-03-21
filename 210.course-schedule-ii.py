#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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

        if len(topo) != V: return []
        
        return topo
        
        
# @lc code=end

