#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
import collections
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u,v,t in times:
            edges[u].append((v, t))

        # init min heap
        pq = []                     # min heap
        heapq.heappush(pq, (0, k))  # (dist, node)


        time2nodes = {}
        while pq:
            time1, node1 = heapq.heappop(pq)

            # if node already visited
            if node1 in time2nodes:
                continue

            # store time 
            time2nodes[node1] = time1

            # BFS
            for adjnode, time2 in edges[node1]:
                if adjnode not in time2nodes:
                    heapq.heappush(pq, (time1 + time2, adjnode))
        
        # were able to reach all nodes
        if len(time2nodes) == n:
            return max(time2nodes.values()) 
        
        # couldn't reach all nodes
        else:
            return -1


# @lc code=end

