#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # constants
        V = len(isConnected)
        visited = [0]*V
        adj = [[] for i in range(V)]

        # making adjList from mat
        for i in range(V):
            for j in range(V):
                if isConnected[i][j] and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)
        
        # dfs func
        def dfs(node):
            visited[node] = 1
            for it in adj[node]:
                if not visited[it]:
                    dfs(it)
        
        # bfs func
        def bfs(node):
            visited[node] = 1
            q = deque([node])
            while q:
                node = q.popleft()
                for it in adj[node]:
                    if not visited[it]:
                        visited[it] = 1
                        q.append(it)
        
        # driver loop
        num_prov = 0
        for node in range(V):
            if not visited[node]:
                num_prov += 1
                # call any traversal
                # dfs(node)
                bfs(node)
        
        return num_prov
        
# @lc code=end

