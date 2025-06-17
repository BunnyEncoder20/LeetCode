#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
from typing import List
from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # making adj list 
        adj = [[] for i in range(n)]
        for i, j, wt in flights:
            adj[i].append((j, wt))


        q = deque()              # cause we using Stops and they are unit increases
        dist = [float('inf')] * n
        dist[src] = 0
        q.append((0, src, 0))     # (stops, node, dist)

        while q:
            stops, node, distance = q.popleft()

            # if we have exceeds number of allowed stops
            if stops > k: continue

            # NOTE we do not stop if we encounter destination
            # casue we might get better dist further down 

            for adjNode, wt in adj[node]:
                if distance + wt < dist[adjNode] and stops <= k:
                    dist[adjNode] = distance + wt
                    q.append((stops+1, adjNode, distance + wt))

        # not able to reach destination
        if dist[dst] == float('inf'):
            return -1

        return dist[dst]
# @lc code=end

